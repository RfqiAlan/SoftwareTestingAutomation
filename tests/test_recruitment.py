"""S07 - Recruitment (TC-REC-01 s/d TC-REC-06)
Diadaptasi dari Tugas3_OrangeHRM.side
"""
import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_tc_rec_01_halaman_candidates(logged_in):
    """TC-REC-01: Halaman Candidates terbuka."""
    page = BasePage(logged_in)
    page.open("/recruitment/viewCandidates")
    page.wait_breadcrumb()
    assert "/recruitment/viewCandidates" in logged_in.current_url


def test_tc_rec_02_cari_kandidat(logged_in):
    """TC-REC-02: Cari kandidat menampilkan hasil."""
    page = BasePage(logged_in)
    page.open("/recruitment/viewCandidates")
    page.click(BasePage.SEARCH)
    assert page.is_visible(BasePage.RECORDS_FOUND) or page.is_visible(BasePage.NO_RECORDS)


def test_tc_rec_03_halaman_vacancies(logged_in):
    """TC-REC-03: Halaman Vacancies terbuka."""
    page = BasePage(logged_in)
    page.open("/recruitment/viewJobVacancy")
    page.wait_breadcrumb()
    assert "/recruitment/viewJobVacancy" in logged_in.current_url


def test_tc_rec_04_add_vacancy_validasi_kolom_wajib(logged_in):
    """TC-REC-04: Add Vacancy - validasi kolom wajib."""
    page = BasePage(logged_in)
    page.open("/recruitment/addJobVacancy")
    page.click(BasePage.SUBMIT)
    assert page.wait_error_count(1) >= 1


def test_tc_rec_05_add_candidate_validasi_kolom_wajib(logged_in):
    """TC-REC-05: Add Candidate - validasi kolom wajib."""
    page = BasePage(logged_in)
    page.open("/recruitment/addCandidate")
    page.click(BasePage.SUBMIT)
    assert page.wait_error_count(1) >= 1


def test_tc_rec_06_add_candidate_berhasil_disimpan(logged_in):
    """TC-REC-06: Add Candidate - berhasil disimpan."""
    page = BasePage(logged_in)
    page.open("/recruitment/addCandidate")
    suffix = str(int(time.time()))[-7:]
    page.type_text((By.NAME, "firstName"), "Selenium")
    page.type_text((By.NAME, "lastName"), f"Cand{suffix}")
    page.type_text((By.XPATH, "//label[text()='Email']/parent::div/following-sibling::div/input"), f"sel{suffix}@example.com")
    page.click(BasePage.SUBMIT)
    page.wait_url_contains("/recruitment/addCandidate/")
    assert "/recruitment/addCandidate/" in logged_in.current_url
