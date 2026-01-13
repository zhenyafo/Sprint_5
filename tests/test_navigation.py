import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestNavigation:
    def test_go_to_personal_account(self, driver):
        main_page = MainPage(driver)
        
        main_page.open()
        main_page.click_personal_account_button()
        
        assert "/login" in driver.current_url
    
    def test_go_from_account_to_constructor(self, driver, test_user_data):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_personal_account_button()
        
        login_page.login(test_user_data["email"], test_user_data["password"])
        
        main_page.click_constructor_button()
        
        assert main_page.is_constructor_page()
    
    def test_go_from_account_by_logo(self, driver, test_user_data):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_personal_account_button()
        
        login_page.login(test_user_data["email"], test_user_data["password"])
        
        main_page.click_logo()
        
        assert main_page.is_constructor_page()