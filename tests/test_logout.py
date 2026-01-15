import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.profile_page_locators import ProfilePageLocators


class TestLogout:
    def test_logout_from_account(self, driver, test_user_data):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        main_page.click_login_button()
        
        login_page.login(test_user_data["email"], test_user_data["password"])
        
        main_page.click_personal_account_button()
        
        logout_button = driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON)
        logout_button.click()

        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url