import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
from pages.registration_page import RegistrationPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestRegistration:
    def test_successful_registration(self, driver, new_user_for_registration):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        registration_page = RegistrationPage(driver)
        
        main_page.open()
        main_page.click_login_button()
        login_page.click_register_link()
        
        registration_page.register_user(
            new_user_for_registration["name"],
            new_user_for_registration["email"],
            new_user_for_registration["password"]
        )
        
        assert "/login" in driver.current_url
    
    def test_registration_with_invalid_password(self, driver):
        from helpers.generators import Generators
        
        registration_page = RegistrationPage(driver)
        
        registration_page.open("register")
        
        registration_page.register_user(
            Generators.generate_name(),
            Generators.generate_email(),
            "123" 
        )

        assert registration_page.is_password_error_displayed()