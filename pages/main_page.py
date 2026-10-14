"""Bagian yang ada di semua halaman setelah login: menu samping dan menu user."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    USER_DROPDOWN = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    DIALOG = (By.CSS_SELECTOR, ".oxd-dialog-sheet")
    CLOSE_DIALOG = (By.CSS_SELECTOR, ".oxd-dialog-close-button")
    DASHBOARD_WIDGET = (By.CSS_SELECTOR, ".orangehrm-dashboard-widget")
    SIDEBAR_SEARCH = (By.XPATH, "//input[@placeholder='Search'] | //div[contains(@class,'oxd-main-menu-search')]//input")
    MENU_ITEMS = (By.CSS_SELECTOR, "a.oxd-main-menu-item")

    @staticmethod
    def sidebar_locator(href_fragment: str):
        # Pakai href supaya tidak tergantung bahasa tampilan.
        return (By.CSS_SELECTOR, f"a.oxd-main-menu-item[href*='{href_fragment}']")

    @staticmethod
    def _menu_item(position: int):
        # Urutan menu user: 1 About, 2 Support, 3 Change Password, 4 Logout
        return (By.XPATH, f"(//ul[contains(@class,'oxd-dropdown-menu')]/li/a)[{position}]")

    def open_module(self, href_fragment: str):
        self.click(self.sidebar_locator(href_fragment))
        self.wait_url_contains(href_fragment)
        self.wait_breadcrumb()

    def open_user_menu(self):
        self.click(self.USER_DROPDOWN)

    def open_about(self):
        self.open_user_menu()
        self.click(self._menu_item(1))
        return self.visible(self.DIALOG)

    def open_support(self):
        self.open_user_menu()
        self.click(self._menu_item(2))

    def open_change_password(self):
        self.open_user_menu()
        self.click(self._menu_item(3))

    def logout(self):
        self.open_user_menu()
        self.click((By.XPATH, "//ul[contains(@class,'oxd-dropdown-menu')]//a[contains(@href,'/auth/logout')]"))
        self.wait_url_contains("/auth/login")

    def dashboard_widget_count(self) -> int:
        self.visible(self.DASHBOARD_WIDGET)
        return len(self.driver.find_elements(*self.DASHBOARD_WIDGET))

    def close_about(self):
        self.click(self.CLOSE_DIALOG)
        self.wait_gone(self.DIALOG)

    def search_sidebar(self, text: str):
        self.type_text(self.SIDEBAR_SEARCH, text)

    def get_visible_menu_items(self):
        return [el for el in self.driver.find_elements(*self.MENU_ITEMS) if el.is_displayed()]
