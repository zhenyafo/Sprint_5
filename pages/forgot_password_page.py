from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class ForgotPasswordPage(BasePage):
    def click_login_link(self):
        self.click_element(LoginPageLocators.LOGIN_LINK)
        