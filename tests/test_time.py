"""S06 - Time & Attendance (TC-TIME-01 s/d TC-TIME-06)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_tc_time_01_halaman_employee_timesheets(logged_in):
    """TC-TIME-01: Halaman Employee Timesheets terbuka."""
    page = BasePage(logged_in)
    page.open("/time/viewEmployeeTimesheet")
    page.wait_breadcrumb()
    assert "/time/viewEmployeeTimesheet" in logged_in.current_url


def test_tc_time_02_employee_timesheets_validasi_pencarian(logged_in):
    """TC-TIME-02: Employee Timesheets - validasi pencarian."""
    page = BasePage(logged_in)
    page.open("/time/viewEmployeeTimesheet")
    page.click((By.XPATH, "//button[normalize-space()='View']"))
    assert page.wait_error_count(1) >= 1


def test_tc_time_03_halaman_my_timesheets(logged_in):
    """TC-TIME-03: Halaman My Timesheets terbuka."""
    page = BasePage(logged_in)
    page.open("/time/viewMyTimesheet")
    page.wait_breadcrumb()
    assert "/time/viewMyTimesheet" in logged_in.current_url


def test_tc_time_04_halaman_attendance_my_records(logged_in):
    """TC-TIME-04: Halaman Attendance My Records terbuka."""
    page = BasePage(logged_in)
    page.open("/attendance/viewMyAttendanceRecord")
    page.wait_breadcrumb()
    assert "/attendance/viewMyAttendanceRecord" in logged_in.current_url


def test_tc_time_05_halaman_customers(logged_in):
    """TC-TIME-05: Halaman Customers terbuka."""
    page = BasePage(logged_in)
    page.open("/time/viewCustomers")
    page.wait_breadcrumb()
    assert "/time/viewCustomers" in logged_in.current_url


def test_tc_time_06_add_customer_validasi_kolom_wajib(logged_in):
    """TC-TIME-06: Add Customer - validasi kolom wajib."""
    page = BasePage(logged_in)
    page.open("/time/addCustomer")
    page.click(BasePage.SUBMIT)
    assert page.wait_error_count(1) >= 1
