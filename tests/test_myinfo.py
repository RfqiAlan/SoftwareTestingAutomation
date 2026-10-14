"""S08 - My Info (TC-MYINFO-01 s/d TC-MYINFO-02)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_tc_myinfo_01_my_info_menampilkan_personal_details(logged_in):
    """TC-MYINFO-01: My Info menampilkan Personal Details."""
    page = BasePage(logged_in)
    page.open("/pim/viewMyDetails")
    page.visible((By.NAME, "firstName"))
    page.wait_url_contains("/pim/viewPersonalDetails")
    assert "/pim/viewPersonalDetails" in logged_in.current_url


def test_tc_myinfo_02_ubah_contact_details(logged_in):
    """TC-MYINFO-02: Ubah Contact Details berhasil disimpan."""
    page = BasePage(logged_in)
    page.open("/pim/viewMyDetails")
    page.click((By.XPATH, "//a[contains(@href,'contactDetails') or normalize-space()='Contact Details']"))
    page.wait_url_contains("/pim/contactDetails")
    page.wait_loader_gone()
    suffix = str(int(time.time()))[-6:]
    street_input = (By.XPATH, "//label[text()='Street 1']/parent::div/following-sibling::div/input")
    page.type_text(street_input, f"Jl. Selenium {suffix}")
    page.click(BasePage.SUBMIT)
    assert page.is_visible(BasePage.TOAST_SUCCESS, timeout=10)
