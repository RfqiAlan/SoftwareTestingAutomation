from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BuzzPage(BasePage):
    POST_BOX = (By.CSS_SELECTOR, "textarea.oxd-buzz-post-input")
    POST_BUTTON = (By.CSS_SELECTOR, ".oxd-buzz-post button[type='submit']")
    BUTTON_POST = (By.XPATH, "//button[normalize-space()='Post']")
    BUTTON_MOST_LIKED = (By.XPATH, "//button[normalize-space()='Most Liked Posts']")

    def create_post(self, text: str):
        self.open("/buzz/viewBuzz")
        self.wait_breadcrumb()
        self.wait_loader_gone()
        box = self.visible(self.POST_BOX)
        box.click()
        box.send_keys(text)
        self.click(self.POST_BUTTON)
        self.wait_loader_gone()

    def wait_post_visible(self, text: str, timeout=25):
        return self.visible((By.XPATH, f"//p[contains(., '{text}')]"), timeout=timeout)
