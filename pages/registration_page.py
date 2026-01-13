from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def enter_name(self, name):
        self.send_keys(RegistrationPageLocators.NAME_INPUT, name)
    
    def enter_email(self, email):
        self.send_keys(RegistrationPageLocators.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        self.send_keys(RegistrationPageLocators.PASSWORD_INPUT, password)
    
    def click_register_button(self):
        self.click_element(RegistrationPageLocators.REGISTER_BUTTON)
    
    def register_user(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register_button()
    
    def click_login_link(self):
        self.click_element(RegistrationPageLocators.LOGIN_LINK)
    
    def is_password_error_displayed(self):
        return self.is_element_present(RegistrationPageLocators.PASSWORD_ERROR)