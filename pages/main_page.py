from turtle import bye
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_login_button(self):
        login_button = self.find_element((By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")) 
        login_button.click()
    
    def click_personal_account_button(self):
        account_button = self.find_element((By.XPATH, "//a[@href='/account']"))
        account_button.click()
    
    def click_constructor_button(self):
        constructor_button = self.find_element((By.XPATH, "//p[text()='Конструктор']"))
        constructor_button.click()
    
    def click_logo(self):
        logo = self.find_element((By.XPATH, "//div[contains(@class, 'logo')]"))
        logo.click()
    
    def click_buns_section(self):
        buns_tab = self.find_element((By.XPATH, "//span[text()='Булки']/parent::div"))
        buns_tab.click()
    
    def click_sauces_section(self):
        sauces_tab = self.find_element((By.XPATH, "//span[text()='Соусы']/parent::div"))
        sauces_tab.click()
    
    def click_toppings_section(self):
        toppings_tab = self.find_element((By.XPATH, "//span[text()='Начинки']/parent::div"))
        toppings_tab.click()
    
    def is_personal_account_button_visible(self):
        try:
            self.find_element((By.XPATH, "//a[@href='/account']"), timeout=3)
            return True
        except:
            return False
    
    def get_active_tab_text(self):
        try:
            active_tab = self.find_element((By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]"), timeout=3)
            return active_tab.text
        except:
            return ""