"""Kelas dasar Page Object: semua aksi dasar (klik, ketik, tunggu) ada di sini."""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import settings


class BasePage:
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    CANCEL = (By.XPATH, "//button[normalize-space()='Cancel']")
    SEARCH = (By.XPATH, "//button[normalize-space()='Search']")
    RESET = (By.XPATH, "//button[normalize-space()='Reset']")
    ADD = (By.XPATH, "//button[normalize-space()='Add']")
    BREADCRUMB = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb-module")
    FIELD_ERROR = (By.CSS_SELECTOR, ".oxd-input-field-error-message")
    TOAST_SUCCESS = (By.CSS_SELECTOR, ".oxd-toast--success")
    TOAST_INFO = (By.CSS_SELECTOR, ".oxd-toast--info")
    RECORDS_FOUND = (By.XPATH, "//span[contains(.,'Found')] | //div[contains(@class,'orangehrm-horizontal-padding')]//span[contains(@class,'oxd-text--span')]")
    NO_RECORDS = (By.XPATH, "//span[text()='No Records Found'] | //div[contains(@class,'oxd-toast--info')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.TIMEOUT)

    # ---- navigasi -------------------------------------------------------
    def open(self, path: str):
        self.driver.get(settings.url(path))

    def wait_url_contains(self, fragment: str, timeout=None):
        WebDriverWait(self.driver, timeout or settings.TIMEOUT).until(
            EC.url_contains(fragment),
            message=f"URL tidak mengandung '{fragment}'. URL sekarang: {self.driver.current_url}",
        )

    def wait_breadcrumb(self):
        return self.visible(self.BREADCRUMB)

    # ---- menunggu elemen ------------------------------------------------
    def visible(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or settings.TIMEOUT).until(
            EC.visibility_of_element_located(locator),
            message=f"Elemen tidak muncul: {locator}",
        )

    def clickable(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or settings.TIMEOUT).until(
            EC.element_to_be_clickable(locator),
            message=f"Elemen tidak bisa diklik: {locator}",
        )

    def is_visible(self, locator, timeout=3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_gone(self, locator, timeout=None):
        WebDriverWait(self.driver, timeout or settings.TIMEOUT).until(
            EC.invisibility_of_element_located(locator)
        )

    # ---- aksi -----------------------------------------------------------
    def click(self, locator):
        self.clickable(locator).click()

    def type_text(self, locator, text: str, clear: bool = True):
        element = self.visible(locator)
        element.click()
        if clear:
            platform = str(self.driver.capabilities.get("platformName", "")).lower()
            modifier = Keys.COMMAND if "mac" in platform else Keys.CONTROL
            element.send_keys(modifier + "a")
            element.send_keys(Keys.DELETE)
        element.send_keys(text)

    def text_of(self, locator) -> str:
        return self.visible(locator).text

    # ---- pesan validasi ---------------------------------------------------
    def visible_error_count(self) -> int:
        return len([e for e in self.driver.find_elements(*self.FIELD_ERROR) if e.is_displayed()])

    def wait_error_count(self, minimum: int) -> int:
        """Tunggu sampai minimal `minimum` pesan error di bawah kolom muncul."""
        WebDriverWait(self.driver, settings.TIMEOUT).until(
            lambda d: self.visible_error_count() >= minimum,
            message=f"Pesan validasi kurang dari {minimum}. Terlihat: {self.visible_error_count()}",
        )
        return self.visible_error_count()
