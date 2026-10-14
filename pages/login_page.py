from selenium.webdriver.common.by import By

import settings
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    ALERT = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    FORGOT = (By.CSS_SELECTOR, ".orangehrm-login-forgot-header")
    TITLE = (By.CSS_SELECTOR, ".orangehrm-login-title")
    FOOTER = (By.CSS_SELECTOR, ".orangehrm-login-footer")
    FOOTER_SOCIAL = (By.CSS_SELECTOR, ".orangehrm-login-footer-sm a")
    DEMO_CREDENTIALS = (By.CSS_SELECTOR, ".orangehrm-demo-credentials")

    def open_login(self):
        self.open("/auth/login")
        self.visible(self.USERNAME, timeout=settings.TIMEOUT * 2)

    def login(self, username: str, password: str):
        if username:
            self.type_text(self.USERNAME, username)
        if password:
            self.type_text(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def wait_for_dashboard(self):
        self.wait_url_contains("/dashboard")
        self.wait_breadcrumb()

    def password_is_masked(self) -> bool:
        return self.visible(self.PASSWORD).get_attribute("type") == "password"

    def click_forgot_password(self):
        self.click(self.FORGOT)
