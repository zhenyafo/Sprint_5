import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class TestLogin:
    def test_login_from_main_page_button(self, driver, test_user_data):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_login_button()
        
        login_page.login(test_user_data["email"], test_user_data["password"])
        
        assert main_page.is_personal_account_button_visible()
    
    def test_login_from_personal_account_button(self, driver, test_user_data):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_personal_account_button()
        
        login_page.login(test_user_data["email"], test_user_data["password"])
        
        assert "/account" in driver.current_url
    
    def test_login_from_registration_page(self, driver, test_user_data):
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        registration_page.open("register")
        registration_page.click_login_link()
        
        login_page.login(test_user_data["email"], test_user_data["password"])
        
        assert "/account" in driver.current_url
    
    def test_login_from_forgot_password_page(self, driver, test_user_data):
        login_page = LoginPage(driver)
        
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        
        from selenium.webdriver.common.by import By
        driver.find_element(By.LINK_TEXT, "Войти").click()
        
        login_page.login(test_user_data["email"], test_user_data["password"])
        
        assert "/account" in driver.current_url