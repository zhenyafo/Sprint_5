import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from pages.registration_page import RegistrationPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from helpers.generators import Generators


class TestRegistration:
    def test_successful_registration(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        registration_page = RegistrationPage(driver)
        
        user_data = {
            "name": Generators.generate_name(),
            "email": Generators.generate_email(),
            "password": Generators.generate_password(8)
        }
        
        main_page.open()
        main_page.click_login_button()
        login_page.click_register_link()
        
        
        registration_page.register_user(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        assert "/login" in driver.current_url
        
        assert login_page.is_login_page()
    
    def test_registration_with_invalid_password(self, driver):
        registration_page = RegistrationPage(driver)
        
        registration_page.open("register")
        
        registration_page.register_user(
            Generators.generate_name(),
            Generators.generate_email(),
            "123"
        )
        
        assert registration_page.is_password_error_displayed()