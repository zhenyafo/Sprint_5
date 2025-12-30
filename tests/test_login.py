import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.forgot_password_page import ForgotPasswordPage


class TestLogin:
    @pytest.fixture
    def pre_registered_user(self, data_generator):
        return {
            "email": data_generator.generate_email(),
            "password": data_generator.generate_password(),
            "name": data_generator.generate_name()
        }
    
    def test_login_from_main_page_button(self, driver, pre_registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_login_button()
        
        login_page.login(pre_registered_user["email"], pre_registered_user["password"])
        
        assert main_page.is_personal_account_button_visible()
    
    def test_login_from_personal_account_button(self, driver, pre_registered_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_personal_account_button()
        
        login_page.login(pre_registered_user["email"], pre_registered_user["password"])
        
        assert "account" in driver.current_url
    
    def test_login_from_registration_page(self, driver, pre_registered_user):
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        registration_page.open("register")
        registration_page.click_login_link()
        
        login_page.login(pre_registered_user["email"], pre_registered_user["password"])
        
        assert "account" in driver.current_url
    
    def test_login_from_forgot_password_page(self, driver, pre_registered_user):
        forgot_password_page = ForgotPasswordPage(driver)
        login_page = LoginPage(driver)
        
        forgot_password_page.open("forgot-password")
        forgot_password_page.click_login_link()
        
        login_page.login(pre_registered_user["email"], pre_registered_user["password"])
        
        assert "account" in driver.current_url