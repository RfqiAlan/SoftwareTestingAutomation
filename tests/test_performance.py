"""S09 - Performance (TC-PERF-01 s/d TC-PERF-05)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
from pages.base_page import BasePage


def test_tc_perf_01_halaman_employee_reviews(logged_in):
    """TC-PERF-01: Halaman Employee Reviews terbuka."""
    page = BasePage(logged_in)
    page.open("/performance/searchEvaluatePerformanceReview")
    page.wait_breadcrumb()
    assert "/performance/searchEvaluatePerformanceReview" in logged_in.current_url


def test_tc_perf_02_cari_employee_reviews(logged_in):
    """TC-PERF-02: Cari Employee Reviews menampilkan hasil."""
    page = BasePage(logged_in)
    page.open("/performance/searchEvaluatePerformanceReview")
    page.click(BasePage.SEARCH)
    assert page.is_visible(BasePage.RECORDS_FOUND) or page.is_visible(BasePage.NO_RECORDS)


def test_tc_perf_03_halaman_my_reviews(logged_in):
    """TC-PERF-03: Halaman My Reviews terbuka."""
    page = BasePage(logged_in)
    page.open("/performance/myPerformanceReview")
    page.wait_breadcrumb()
    assert "/performance/myPerformanceReview" in logged_in.current_url


def test_tc_perf_04_halaman_kpis(logged_in):
    """TC-PERF-04: Halaman KPIs terbuka."""
    page = BasePage(logged_in)
    page.open("/performance/searchKpi")
    page.wait_breadcrumb()
    assert "/performance/searchKpi" in logged_in.current_url


def test_tc_perf_05_add_kpi_validasi_kolom_wajib(logged_in):
    """TC-PERF-05: Add KPI - validasi kolom wajib."""
    page = BasePage(logged_in)
    page.open("/performance/saveKpi")
    page.click(BasePage.SUBMIT)
    assert page.wait_error_count(1) >= 1
