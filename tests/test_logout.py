import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogout:
    def test_logout_from_account(self, driver, register_new_user):
        
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open()
        main_page.click_login_button()
        login_page.login(
            register_new_user["email"], 
            register_new_user["password"]
        )

        main_page.click_personal_account_button()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        logout_button = driver.find_element(By.XPATH, "//button[text()='Выход']")
        logout_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in driver.current_url
        
        assert driver.find_element(By.XPATH, "//h2[text()='Вход']").is_displayed() 