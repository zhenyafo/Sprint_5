import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from pages.registration_page import RegistrationPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestRegistration:
    def test_successful_registration(self, driver, data_generator):
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_login_button()
        
        registration_page.click_login_link()
        
        user_data = {
            "name": data_generator.generate_name(),
            "email": data_generator.generate_email(),
            "password": data_generator.generate_password(8)
        }
        
        registration_page.register_user(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        assert login_page.is_login_page()
    
    def test_registration_with_invalid_password(self, driver, data_generator):
        registration_page = RegistrationPage(driver)
        registration_page.open("register")
        
        registration_page.register_user(
            data_generator.generate_name(),
            data_generator.generate_email(),
            "123"
        )
        
        assert registration_page.is_password_error_displayed()
        
