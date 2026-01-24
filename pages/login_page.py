from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
    
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    
    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)
    
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
        
