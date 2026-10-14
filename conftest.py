"""Fixture bersama: membuat browser (lokal atau Selenium Grid), login, dan screenshot saat gagal."""
import base64
import os
import re

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import settings
from pages.login_page import LoginPage

SCREENSHOT_DIR = os.path.join("reports", "screenshots")


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=os.getenv("HEADLESS", "") == "1",
        help="Jalankan Chrome tanpa jendela (untuk CI / server).",
    )
    parser.addoption(
        "--grid-url",
        action="store",
        default=os.getenv("GRID_URL", ""),
        help="Alamat Selenium Grid, contoh: http://localhost:4444",
    )


def pytest_configure(config):
    # Tampilkan info tambahan di bagian atas laporan HTML.
    try:
        from pytest_metadata.plugin import metadata_key

        meta = config.stash[metadata_key]
        meta["Base URL"] = settings.BASE_URL
        meta["Mode"] = "Selenium Grid" if config.getoption("--grid-url") else "Chrome lokal"
        meta["Headless"] = str(config.getoption("--headless"))
    except Exception:
        pass


def pytest_html_report_title(report):
    report.title = "Laporan Tugas 4 - Selenium WebDriver - OrangeHRM"


def _build_options(headless: bool, use_grid: bool) -> Options:
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    if headless or use_grid:
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1366,768")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-US")
    return options


@pytest.fixture
def driver(request):
    """Satu browser baru untuk setiap tes (supaya tes tidak saling mengganggu)."""
    grid_url = request.config.getoption("--grid-url")
    headless = request.config.getoption("--headless")
    options = _build_options(headless, bool(grid_url))

    if grid_url:
        drv = webdriver.Remote(command_executor=grid_url, options=options)
    else:
        drv = webdriver.Chrome(options=options)

    drv.implicitly_wait(0)  # kita pakai explicit wait saja
    request.node._driver = drv
    yield drv
    drv.quit()


@pytest.fixture
def logged_in(driver):
    """Browser yang sudah login sebagai Admin dan berada di Dashboard."""
    page = LoginPage(driver)
    page.open_login()
    page.login(settings.USERNAME, settings.PASSWORD)
    page.wait_for_dashboard()
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Kalau tes gagal: simpan screenshot dan tempelkan ke laporan HTML."""
    outcome = yield
    report = outcome.get_result()
    if report.when not in ("setup", "call") or not report.failed:
        return
    drv = getattr(item, "_driver", None)
    if drv is None:
        return
    try:
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        name = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)[-120:]
        path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
        drv.save_screenshot(path)
        with open(path, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode()
        from pytest_html import extras

        report.extras = getattr(report, "extras", []) + [extras.png(b64, "Screenshot saat gagal")]
    except Exception:
        pass  # screenshot gagal tidak boleh menutupi error asli
