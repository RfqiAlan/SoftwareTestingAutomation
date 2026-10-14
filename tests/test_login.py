"""S01 - Login & Autentikasi (TC-LOGIN-01 s/d TC-LOGIN-16)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import settings
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.smoke
def test_tc_login_01_login_valid(driver):
    """TC-LOGIN-01: Login valid."""
    page = LoginPage(driver)
    page.open_login()
    page.login(settings.USERNAME, settings.PASSWORD)
    page.wait_for_dashboard()
    assert "OrangeHRM" in driver.title
    assert page.is_visible(LoginPage.BREADCRUMB)
    assert page.is_visible((By.XPATH, "//h6[normalize-space()='Dashboard']"))
    assert "/dashboard" in driver.current_url

    # Verifikasi logout di akhir
    MainPage(driver).logout()
    assert "/auth/login" in driver.current_url


@pytest.mark.smoke
def test_tc_login_02_password_salah(driver):
    """TC-LOGIN-02: Password salah."""
    page = LoginPage(driver)
    page.open_login()
    page.login("Admin", "salah123")
    assert page.is_visible(LoginPage.ALERT, timeout=10)
    assert "/auth/login" in driver.current_url


def test_tc_login_03_username_salah(driver):
    """TC-LOGIN-03: Username salah."""
    page = LoginPage(driver)
    page.open_login()
    page.login("userngawur", "admin123")
    assert page.is_visible(LoginPage.ALERT, timeout=10)
    assert "/auth/login" in driver.current_url


def test_tc_login_04_username_dan_password_salah(driver):
    """TC-LOGIN-04: Username dan password salah."""
    page = LoginPage(driver)
    page.open_login()
    page.login("userngawur", "salah123")
    assert page.is_visible(LoginPage.ALERT, timeout=10)
    assert "/auth/login" in driver.current_url


def test_tc_login_05_password_beda_huruf_besar_kecil(driver):
    """TC-LOGIN-05: Password beda huruf besar/kecil."""
    page = LoginPage(driver)
    page.open_login()
    page.login("admin", "ADMIN123")
    assert page.is_visible(LoginPage.ALERT, timeout=10)
    assert "/auth/login" in driver.current_url


def test_tc_login_06_input_sql_injection_ditolak(driver):
    """TC-LOGIN-06: Input SQL injection ditolak."""
    page = LoginPage(driver)
    page.open_login()
    page.login("' OR '1'='1", "' OR '1'='1")
    assert page.is_visible(LoginPage.ALERT, timeout=10)
    assert "/auth/login" in driver.current_url


@pytest.mark.smoke
def test_tc_login_07_username_dan_password_kosong(driver):
    """TC-LOGIN-07: Username dan password kosong."""
    page = LoginPage(driver)
    page.open_login()
    page.click(LoginPage.SUBMIT)
    assert page.wait_error_count(2) >= 2


def test_tc_login_08_password_kosong(driver):
    """TC-LOGIN-08: Password kosong."""
    page = LoginPage(driver)
    page.open_login()
    page.type_text(LoginPage.USERNAME, "Admin")
    page.click(LoginPage.SUBMIT)
    assert page.wait_error_count(1) == 1


def test_tc_login_09_username_kosong(driver):
    """TC-LOGIN-09: Username kosong."""
    page = LoginPage(driver)
    page.open_login()
    page.type_text(LoginPage.PASSWORD, "admin123")
    page.click(LoginPage.SUBMIT)
    assert page.wait_error_count(1) == 1


def test_tc_login_10_login_dengan_submit_form(driver):
    """TC-LOGIN-10: Login dengan submit form (setara Enter)."""
    page = LoginPage(driver)
    page.open_login()
    page.type_text(LoginPage.USERNAME, settings.USERNAME)
    pw_field = page.visible(LoginPage.PASSWORD)
    pw_field.send_keys(settings.PASSWORD)
    pw_field.send_keys(Keys.ENTER)
    page.wait_for_dashboard()
    assert "/dashboard" in driver.current_url
    MainPage(driver).logout()
    assert "/auth/login" in driver.current_url


def test_tc_login_11_password_tersamarkan(driver):
    """TC-LOGIN-11: Password tersamarkan."""
    page = LoginPage(driver)
    page.open_login()
    assert page.password_is_masked()


@pytest.mark.smoke
def test_tc_login_12_logout(driver):
    """TC-LOGIN-12: Logout."""
    page = LoginPage(driver)
    page.open_login()
    page.login(settings.USERNAME, settings.PASSWORD)
    page.wait_for_dashboard()
    MainPage(driver).logout()
    assert "/auth/login" in driver.current_url
    assert page.is_visible(LoginPage.TITLE)


def test_tc_login_13_akses_halaman_terproteksi_tanpa_login(driver):
    """TC-LOGIN-13: Akses halaman terproteksi tanpa login."""
    page = LoginPage(driver)
    page.open("/auth/logout")
    page.open("/dashboard/index")
    page.wait_url_contains("/auth/login")
    assert "/auth/login" in driver.current_url


def test_tc_login_14_halaman_lupa_password_terbuka(driver):
    """TC-LOGIN-14: Halaman Lupa Password terbuka."""
    page = LoginPage(driver)
    page.open_login()
    page.click_forgot_password()
    page.wait_url_contains("/auth/requestPasswordResetCode")
    assert page.is_visible(LoginPage.SUBMIT)
    assert "requestPasswordResetCode" in driver.current_url


def test_tc_login_15_lupa_password_username_kosong(driver):
    """TC-LOGIN-15: Lupa Password - username kosong."""
    page = LoginPage(driver)
    page.open("/auth/requestPasswordResetCode")
    page.visible(LoginPage.SUBMIT)
    page.click(LoginPage.SUBMIT)
    assert page.wait_error_count(1) >= 1


def test_tc_login_16_lupa_password_tombol_cancel(driver):
    """TC-LOGIN-16: Lupa Password - tombol Cancel."""
    page = LoginPage(driver)
    page.open("/auth/requestPasswordResetCode")
    page.click(page.CANCEL)
    page.wait_url_contains("/auth/login")
    assert "/auth/login" in driver.current_url


# Alias untuk kompatibilitas ke belakang
test_login_valid = test_tc_login_01_login_valid
test_logout = test_tc_login_12_logout
test_lupa_password = test_tc_login_14_halaman_lupa_password_terbuka
