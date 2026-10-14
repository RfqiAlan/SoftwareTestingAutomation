"""S02 - UI Halaman Login & Responsif (TC-UI-01 s/d TC-UI-06)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def test_tc_ui_01_judul_halaman_login(driver):
    """TC-UI-01: Judul halaman login adalah OrangeHRM."""
    page = LoginPage(driver)
    page.open_login()
    assert driver.title == "OrangeHRM"


def test_tc_ui_02_elemen_utama_halaman_login(driver):
    """TC-UI-02: Judul Login, tombol submit, dan tautan lupa password tampil."""
    page = LoginPage(driver)
    page.open_login()
    assert page.is_visible(LoginPage.TITLE)
    assert page.is_visible(LoginPage.SUBMIT)
    assert page.is_visible(LoginPage.FORGOT)


def test_tc_ui_03_petunjuk_kredensial_demo_tampil(driver):
    """TC-UI-03: Halaman login demo menampilkan petunjuk username dan password."""
    page = LoginPage(driver)
    page.open_login()
    text = driver.page_source
    assert "Username : Admin" in text or page.is_visible((By.XPATH, "//*[contains(normalize-space(.),'Username : Admin')]"))
    assert "Password : admin123" in text or page.is_visible((By.XPATH, "//*[contains(normalize-space(.),'Password : admin123')]"))


def test_tc_ui_04_footer_dan_tautan_sosial(driver):
    """TC-UI-04: Footer dan tautan sosial tampil."""
    page = LoginPage(driver)
    page.open_login()
    assert page.is_visible(LoginPage.FOOTER)
    assert len(driver.find_elements(*LoginPage.FOOTER_SOCIAL)) >= 1


def test_tc_ui_05_tampilan_mobile(driver):
    """TC-UI-05: Tampilan mobile (375x812) - form login tetap tampil utuh."""
    page = LoginPage(driver)
    driver.set_window_size(375, 812)
    page.open_login()
    assert page.is_visible(LoginPage.USERNAME)
    assert page.is_visible(LoginPage.PASSWORD)
    assert page.is_visible(LoginPage.SUBMIT)
    driver.set_window_size(1366, 768)


def test_tc_ui_06_tampilan_tablet(driver):
    """TC-UI-06: Tampilan tablet (768x1024) - form login tetap tampil utuh."""
    page = LoginPage(driver)
    driver.set_window_size(768, 1024)
    page.open_login()
    assert page.is_visible(LoginPage.USERNAME)
    assert page.is_visible(LoginPage.PASSWORD)
    assert page.is_visible(LoginPage.SUBMIT)
    driver.set_window_size(1366, 768)
