from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)
    
    def click_personal_account_button(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    def click_logo(self):
        self.click_element(MainPageLocators.LOGO)
    
    def click_buns_section(self):
        self.click_element(MainPageLocators.BUNS_SECTION)
    
    def click_sauces_section(self):
        self.click_element(MainPageLocators.SAUCES_SECTION)
    
    def click_toppings_section(self):
        self.click_element(MainPageLocators.TOPPINGS_SECTION)
    
    def is_personal_account_button_visible(self):
        return self.is_element_present(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)