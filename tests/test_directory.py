"""S11 - Directory (TC-DIR-01 s/d TC-DIR-02)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_tc_dir_01_pencarian_direktori(logged_in):
    """TC-DIR-01: Pencarian direktori menampilkan hasil."""
    page = BasePage(logged_in)
    page.open("/directory/viewDirectory")
    page.click(BasePage.SEARCH)
    assert page.is_visible(BasePage.RECORDS_FOUND) or page.is_visible((By.CSS_SELECTOR, ".orangehrm-directory-card"))


def test_tc_dir_02_pencarian_dengan_nama_tidak_valid(logged_in):
    """TC-DIR-02: Pencarian dengan nama tidak valid menampilkan pesan Invalid."""
    page = BasePage(logged_in)
    page.open("/directory/viewDirectory")
    hint_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
    page.type_text(hint_input, "zzzqwe")
    page.click(BasePage.SEARCH)
    assert page.is_visible((By.XPATH, "//span[text()='Invalid']"), timeout=10)
