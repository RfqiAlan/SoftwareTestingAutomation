from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import settings
from pages.base_page import BasePage


class PimPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "input[name='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='lastName']")
    # Kolom form Add Employee: First, Middle, Last, Employee Id (ke-4)
    EMPLOYEE_ID_ADD = (By.XPATH, "(//form//input[contains(@class,'oxd-input')])[4]")
    EMP_ID_FILTER = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
    FILTER_INPUTS = (By.CSS_SELECTOR, ".oxd-table-filter input.oxd-input")
    FILTER_SEARCH = (By.CSS_SELECTOR, ".oxd-table-filter button[type='submit']")
    ROWS = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-card")
    TRASH = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-card .bi-trash")
    CONFIRM_DELETE = (By.CSS_SELECTOR, ".orangehrm-modal-footer .oxd-button--label-danger")

    def open_list(self):
        self.open("/pim/viewEmployeeList")
        self.wait_breadcrumb()
        self.visible(self.FILTER_SEARCH)

    def open_add(self):
        self.open("/pim/addEmployee")
        self.wait_breadcrumb()
        self.visible(self.FIRST_NAME)
        self.wait_loader_gone()

    def submit_empty_form(self):
        self.click(self.SUBMIT)

    def add_employee(self, first: str, last: str, emp_id: str):
        self.open_add()
        self.type_text(self.FIRST_NAME, first)
        self.type_text(self.LAST_NAME, last)
        # ID otomatis terisi setelah halaman selesai dimuat; tunggu dulu baru ganti.
        id_box = self.visible(self.EMPLOYEE_ID_ADD)
        WebDriverWait(self.driver, settings.TIMEOUT).until(
            lambda d: id_box.get_attribute("value") != "", message="ID otomatis tidak terisi"
        )
        self.type_text(self.EMPLOYEE_ID_ADD, emp_id)
        self.click(self.SUBMIT)
        # Simpan berhasil -> pindah ke halaman Personal Details (butuh waktu lebih lama).
        self.wait_url_contains("/pim/viewPersonalDetails", timeout=settings.TIMEOUT * 2)

    def search_by_id(self, emp_id: str):
        self.open_list()
        # input[0] = Employee Name, input[1] = Employee Id
        WebDriverWait(self.driver, settings.TIMEOUT).until(
            lambda d: len(d.find_elements(*self.FILTER_INPUTS)) >= 2
        )
        box = self.driver.find_elements(*self.FILTER_INPUTS)[1]
        box.click()
        box.clear()
        box.send_keys(emp_id)
        self.click(self.FILTER_SEARCH)
        self.wait_loader_gone()

    def _rows_text(self):
        try:
            return [r.text for r in self.driver.find_elements(*self.ROWS)]
        except StaleElementReferenceException:
            return []

    def wait_rows_contain(self, text: str):
        self.wait_loader_gone()
        WebDriverWait(
            self.driver,
            settings.TIMEOUT,
            ignored_exceptions=(StaleElementReferenceException,),
        ).until(
            lambda d: (rows := self._rows_text()) and all(text in r for r in rows),
            message=f"Hasil pencarian tidak memuat '{text}'",
        )
        return len(self._rows_text())

    def wait_no_records(self):
        self.wait_loader_gone()
        WebDriverWait(
            self.driver,
            settings.TIMEOUT,
            ignored_exceptions=(StaleElementReferenceException,),
        ).until(
            lambda d: len(self._rows_text()) == 0 or self.is_visible(self.TOAST_INFO, timeout=1),
            message="Pesan 'tidak ada data' tidak muncul",
        )
        return len(self._rows_text())

    def delete_first_result(self):
        self.click(self.TRASH)
        self.click(self.CONFIRM_DELETE)
        self.visible(self.TOAST_SUCCESS)
