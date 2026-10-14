from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import settings
from pages.base_page import BasePage


class AdminPage(BasePage):
    FILTER_INPUTS = (By.CSS_SELECTOR, ".oxd-table-filter input.oxd-input")
    FILTER_SEARCH = (By.CSS_SELECTOR, ".oxd-table-filter button[type='submit']")
    USERNAME_FILTER = (By.XPATH, "//label[text()='Username']/parent::div/following-sibling::div/input")
    BUTTON_RESET = (By.XPATH, "//button[normalize-space()='Reset']")
    BUTTON_ADD = (By.XPATH, "//button[normalize-space()='Add']")
    ROWS = (By.CSS_SELECTOR, ".oxd-table-body .oxd-table-card")

    def open_users(self):
        self.open("/admin/viewSystemUsers")
        self.wait_breadcrumb()
        self.visible(self.FILTER_SEARCH)

    def open_add_user(self):
        self.open("/admin/saveSystemUser")
        self.wait_breadcrumb()
        self.visible(self.SUBMIT)

    def submit_empty_form(self):
        self.click(self.SUBMIT)

    def search_username(self, username: str):
        box = self.visible(self.FILTER_INPUTS)  # input pertama = Username
        box.click()
        box.clear()
        box.send_keys(username)
        self.click(self.FILTER_SEARCH)

    def _rows_text(self):
        return [r.text.lower() for r in self.driver.find_elements(*self.ROWS)]

    def wait_rows_match(self, text: str):
        """Tunggu sampai daftar hanya berisi baris yang memuat `text`."""
        WebDriverWait(self.driver, settings.TIMEOUT).until(
            lambda d: (rows := self._rows_text()) and all(text.lower() in r for r in rows),
            message=f"Hasil pencarian tidak memuat '{text}'",
        )
        return len(self._rows_text())

    def wait_no_records(self):
        """Tidak ada data: tabel kosong atau muncul toast info 'No Records Found'."""
        WebDriverWait(self.driver, settings.TIMEOUT).until(
            lambda d: len(self._rows_text()) == 0 or self.is_visible(self.TOAST_INFO, timeout=1),
            message="Pesan 'tidak ada data' tidak muncul",
        )
        return len(self._rows_text())
