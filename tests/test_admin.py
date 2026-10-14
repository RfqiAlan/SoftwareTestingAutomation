"""S03 - Admin (TC-ADMIN-01 s/d TC-ADMIN-12)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
import pytest
from selenium.webdriver.common.by import By

from pages.admin_page import AdminPage


def test_tc_admin_01_halaman_user_management(logged_in):
    """TC-ADMIN-01: Halaman User Management terbuka dan tombol Add tampil."""
    admin = AdminPage(logged_in)
    admin.open_users()
    assert admin.is_visible(AdminPage.BREADCRUMB)
    assert admin.is_visible(AdminPage.BUTTON_ADD)


@pytest.mark.smoke
def test_tc_admin_02_cari_user_admin(logged_in):
    """TC-ADMIN-02: Cari user Admin menampilkan hasil."""
    admin = AdminPage(logged_in)
    admin.open_users()
    admin.search_username("Admin")
    assert admin.wait_rows_match("admin") >= 1


def test_tc_admin_03_cari_user_tidak_ada(logged_in):
    """TC-ADMIN-03: Cari user yang tidak ada menampilkan pesan No Records Found."""
    admin = AdminPage(logged_in)
    admin.open_users()
    admin.search_username("zzzqqq999")
    assert admin.wait_no_records() == 0


def test_tc_admin_04_tombol_reset_mengosongkan_filter(logged_in):
    """TC-ADMIN-04: Tombol Reset mengosongkan kolom filter."""
    admin = AdminPage(logged_in)
    admin.open_users()
    box = admin.visible(AdminPage.USERNAME_FILTER)
    box.click()
    box.send_keys("Admin")
    admin.click(AdminPage.BUTTON_RESET)
    admin.wait.until(lambda d: admin.visible(AdminPage.USERNAME_FILTER).get_attribute("value") == "")
    assert admin.visible(AdminPage.USERNAME_FILTER).get_attribute("value") == ""


def test_tc_admin_05_add_user_validasi_kolom_wajib(logged_in):
    """TC-ADMIN-05: Add User - validasi kolom wajib."""
    admin = AdminPage(logged_in)
    admin.open_add_user()
    admin.submit_empty_form()
    assert admin.wait_error_count(1) >= 1
    assert "/admin/saveSystemUser" in logged_in.current_url


def test_tc_admin_06_add_user_cancel_kembali_ke_daftar(logged_in):
    """TC-ADMIN-06: Add User - tombol Cancel kembali ke daftar."""
    admin = AdminPage(logged_in)
    admin.open_add_user()
    admin.click(AdminPage.CANCEL)
    admin.wait_url_contains("/admin/viewSystemUsers")
    assert "/admin/viewSystemUsers" in logged_in.current_url


def test_tc_admin_07_halaman_job_titles(logged_in):
    """TC-ADMIN-07: Halaman Job Titles terbuka."""
    admin = AdminPage(logged_in)
    admin.open("/admin/viewJobTitleList")
    admin.wait_breadcrumb()
    assert "/admin/viewJobTitleList" in logged_in.current_url


def test_tc_admin_08_halaman_pay_grades(logged_in):
    """TC-ADMIN-08: Halaman Pay Grades terbuka."""
    admin = AdminPage(logged_in)
    admin.open("/admin/viewPayGrades")
    admin.wait_breadcrumb()
    assert "/admin/viewPayGrades" in logged_in.current_url


def test_tc_admin_09_halaman_employment_status(logged_in):
    """TC-ADMIN-09: Halaman Employment Status terbuka."""
    admin = AdminPage(logged_in)
    admin.open("/admin/employmentStatus")
    admin.wait_breadcrumb()
    assert "/admin/employmentStatus" in logged_in.current_url


def test_tc_admin_10_halaman_locations(logged_in):
    """TC-ADMIN-10: Halaman Locations terbuka."""
    admin = AdminPage(logged_in)
    admin.open("/admin/viewLocations")
    admin.wait_breadcrumb()
    assert "/admin/viewLocations" in logged_in.current_url


def test_tc_admin_11_halaman_nationalities(logged_in):
    """TC-ADMIN-11: Halaman Nationalities terbuka."""
    admin = AdminPage(logged_in)
    admin.open("/admin/nationality")
    admin.wait_breadcrumb()
    assert "/admin/nationality" in logged_in.current_url


def test_tc_admin_12_halaman_general_information(logged_in):
    """TC-ADMIN-12: Halaman General Information terbuka."""
    admin = AdminPage(logged_in)
    admin.open("/admin/viewOrganizationGeneralInformation")
    admin.wait_breadcrumb()
    assert "/admin/viewOrganizationGeneralInformation" in logged_in.current_url
