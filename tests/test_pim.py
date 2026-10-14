"""S04 - PIM (TC-PIM-01 s/d TC-PIM-06)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
from pages.pim_page import PimPage


def test_tc_pim_01_daftar_karyawan_tampil(logged_in):
    """TC-PIM-01: Daftar karyawan tampil."""
    pim = PimPage(logged_in)
    pim.open_list()
    assert pim.is_visible(PimPage.BREADCRUMB)
    assert pim.is_visible(PimPage.RECORDS_FOUND)


def test_tc_pim_02_cari_karyawan_id_tidak_ada(logged_in):
    """TC-PIM-02: Cari karyawan dengan ID tidak ada."""
    pim = PimPage(logged_in)
    pim.open_list()
    pim.type_text(PimPage.EMP_ID_FILTER, "ZZZ99999")
    pim.click(PimPage.FILTER_SEARCH)
    assert pim.wait_no_records() == 0


def test_tc_pim_03_add_employee_validasi_kolom_wajib(logged_in):
    """TC-PIM-03: Add Employee - validasi kolom wajib."""
    pim = PimPage(logged_in)
    pim.open_add()
    pim.submit_empty_form()
    assert pim.wait_error_count(2) >= 2


def test_tc_pim_04_add_employee_cancel_kembali_ke_daftar(logged_in):
    """TC-PIM-04: Add Employee - Cancel kembali ke daftar."""
    pim = PimPage(logged_in)
    pim.open_add()
    pim.click(PimPage.CANCEL)
    pim.wait_url_contains("/pim/viewEmployeeList")
    assert "/pim/viewEmployeeList" in logged_in.current_url


def test_tc_pim_06_halaman_pim_reports(logged_in):
    """TC-PIM-06: Halaman PIM Reports terbuka."""
    pim = PimPage(logged_in)
    pim.open("/pim/viewDefinedPredefinedReports")
    pim.wait_breadcrumb()
    assert "/pim/viewDefinedPredefinedReports" in logged_in.current_url
