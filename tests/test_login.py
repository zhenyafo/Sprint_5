import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    def test_login_from_main_page_button(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_login_button()
        
        login_page.login(
            registered_user["email"], 
            registered_user["password"]
        )
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
    
    def test_login_from_personal_account_button(self, driver, registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_personal_account_button()
        
        login_page.login(
            registered_user["email"], 
            registered_user["password"]
        )
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
    
    def test_login_from_registration_page(self, driver, registered_user):
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        registration_page.open("register")
        registration_page.click_login_link()
        
        login_page.login(
            registered_user["email"], 
            registered_user["password"]
        )
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"
    
    def test_login_from_forgot_password_page(self, driver, registered_user):
        login_page = LoginPage(driver)
        
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        
        driver.find_element(By.LINK_TEXT, "Войти").click()
        
        login_page.login(
            registered_user["email"], 
            registered_user["password"]
        )

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        assert driver.current_url == "https://stellarburgers.education-services.ru/"