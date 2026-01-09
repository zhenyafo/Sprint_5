from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ForgotPasswordPage(BasePage):
    def click_login_link(self):
        login_link = self.find_element((By.XPATH, "//a[@href='/login']"))
        login_link.click()