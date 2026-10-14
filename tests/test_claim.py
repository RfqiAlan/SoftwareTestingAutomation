"""S13 - Claim (TC-CLAIM-01 s/d TC-CLAIM-05)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
from pages.base_page import BasePage


def test_tc_claim_01_halaman_employee_claims(logged_in):
    """TC-CLAIM-01: Halaman Employee Claims terbuka."""
    page = BasePage(logged_in)
    page.open("/claim/viewAssignClaim")
    page.wait_breadcrumb()
    assert "/claim/viewAssignClaim" in logged_in.current_url


def test_tc_claim_02_cari_employee_claims(logged_in):
    """TC-CLAIM-02: Cari Employee Claims menampilkan hasil."""
    page = BasePage(logged_in)
    page.open("/claim/viewAssignClaim")
    page.click(BasePage.SEARCH)
    assert page.is_visible(BasePage.RECORDS_FOUND) or page.is_visible(BasePage.NO_RECORDS)


def test_tc_claim_03_submit_claim_validasi_kolom_wajib(logged_in):
    """TC-CLAIM-03: Submit Claim - validasi kolom wajib."""
    page = BasePage(logged_in)
    page.open("/claim/submitClaim")
    page.click(BasePage.SUBMIT)
    assert page.wait_error_count(1) >= 1


def test_tc_claim_04_halaman_claim_events(logged_in):
    """TC-CLAIM-04: Halaman Claim Events terbuka."""
    page = BasePage(logged_in)
    page.open("/claim/viewEvents")
    page.wait_breadcrumb()
    assert "/claim/viewEvents" in logged_in.current_url


def test_tc_claim_05_add_event_validasi_kolom_wajib(logged_in):
    """TC-CLAIM-05: Add Event - validasi kolom wajib."""
    page = BasePage(logged_in)
    page.open("/claim/saveEvents")
    page.click(BasePage.SUBMIT)
    assert page.wait_error_count(1) >= 1
