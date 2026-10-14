"""S05 - Leave (TC-LEAVE-01 s/d TC-LEAVE-08)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
from pages.base_page import BasePage


def test_tc_leave_01_halaman_leave_list(logged_in):
    """TC-LEAVE-01: Halaman Leave List terbuka."""
    page = BasePage(logged_in)
    page.open("/leave/viewLeaveList")
    page.wait_breadcrumb()
    assert "/leave/viewLeaveList" in logged_in.current_url


def test_tc_leave_02_cari_leave_list(logged_in):
    """TC-LEAVE-02: Cari Leave List menampilkan data atau pesan informasi."""
    page = BasePage(logged_in)
    page.open("/leave/viewLeaveList")
    page.click(BasePage.SEARCH)
    assert page.is_visible(BasePage.RECORDS_FOUND) or page.is_visible(BasePage.NO_RECORDS)


def test_tc_leave_03_halaman_apply_leave(logged_in):
    """TC-LEAVE-03: Halaman Apply Leave terbuka."""
    page = BasePage(logged_in)
    page.open("/leave/applyLeave")
    page.wait_breadcrumb()
    assert "/leave/applyLeave" in logged_in.current_url


def test_tc_leave_04_halaman_my_leave(logged_in):
    """TC-LEAVE-04: Halaman My Leave terbuka."""
    page = BasePage(logged_in)
    page.open("/leave/viewMyLeaveList")
    page.wait_breadcrumb()
    assert "/leave/viewMyLeaveList" in logged_in.current_url


def test_tc_leave_05_assign_leave_validasi_kolom_wajib(logged_in):
    """TC-LEAVE-05: Assign Leave - validasi kolom wajib."""
    page = BasePage(logged_in)
    page.open("/leave/assignLeave")
    page.click(BasePage.SUBMIT)
    assert page.wait_error_count(1) >= 1


def test_tc_leave_06_leave_entitlements_validasi_pencarian(logged_in):
    """TC-LEAVE-06: Leave Entitlements - validasi pencarian."""
    page = BasePage(logged_in)
    page.open("/leave/viewLeaveEntitlements")
    page.click(BasePage.SEARCH)
    assert page.wait_error_count(1) >= 1


def test_tc_leave_07_halaman_leave_types(logged_in):
    """TC-LEAVE-07: Halaman Leave Types terbuka."""
    page = BasePage(logged_in)
    page.open("/leave/leaveTypeList")
    page.wait_breadcrumb()
    assert "/leave/leaveTypeList" in logged_in.current_url


def test_tc_leave_08_add_leave_type_validasi_kolom_wajib(logged_in):
    """TC-LEAVE-08: Add Leave Type - validasi kolom wajib."""
    page = BasePage(logged_in)
    page.open("/leave/defineLeaveType")
    page.click(BasePage.SUBMIT)
    assert page.wait_error_count(1) >= 1
