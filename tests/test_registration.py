import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from pages.registration_page import RegistrationPage
from pages.main_page import MainPage


class TestRegistration:
    def test_successful_registration(self, driver, random_user_data):
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        
        main_page.open()
        main_page.click_login_button()
        
        registration_page.click_login_link()
        
        registration_page.register_user(
            random_user_data["name"],
            random_user_data["email"],
            random_user_data["password"]
        )
        
        assert "login" in driver.current_url
    
    def test_registration_with_invalid_password(self, driver, data_generator):
        registration_page = RegistrationPage(driver)
        registration_page.open("register")
        
        registration_page.register_user(
            data_generator.generate_name(),
            data_generator.generate_email(),
            data_generator.generate_invalid_password()
        )
        
        assert registration_page.is_password_error_displayed()





        