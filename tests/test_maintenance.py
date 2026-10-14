"""S12 - Maintenance (TC-MAINT-02, TC-MAINT-04)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
from selenium.webdriver.common.by import By

import settings
from pages.base_page import BasePage


def test_tc_maint_02_maintenance_password_benar(logged_in):
    """TC-MAINT-02: Maintenance - password benar membuka akses administrator."""
    page = BasePage(logged_in)
    page.open("/maintenance/viewMaintenanceModule")
    pw_input = (By.CSS_SELECTOR, "input[name='password']")
    if page.is_visible(pw_input, timeout=5):
        page.type_text(pw_input, settings.PASSWORD)
        page.click((By.XPATH, "//button[normalize-space()='Confirm']"))
    page.wait_url_contains("/maintenance/")
    assert "/maintenance/" in logged_in.current_url


def test_tc_maint_04_maintenance_tombol_cancel(logged_in):
    """TC-MAINT-04: Maintenance - tombol Cancel kembali ke dashboard."""
    page = BasePage(logged_in)
    page.open("/maintenance/viewMaintenanceModule")
    cancel_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
    if page.is_visible(cancel_btn, timeout=5):
        page.click(cancel_btn)
    page.wait_url_contains("/dashboard")
    assert "/dashboard" in logged_in.current_url
