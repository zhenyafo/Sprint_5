import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from data.test_data import test_data


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    user_data = test_data.EXISTING_USER
    
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    from pages.registration_page import RegistrationPage
    
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    registration_page = RegistrationPage(driver)
    
    main_page.open()
    main_page.click_login_button()
    
    try:
        login_page.login(user_data["email"], user_data["password"])
        return user_data
    except:
 
        main_page.open()
        main_page.click_login_button()
        login_page.click_register_link()
        
        registration_page.register_user(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        
        return user_data


@pytest.fixture
def new_user_for_registration():
    from helpers.generators import Generators
    
    return {
        "name": Generators.generate_name(),
        "email": Generators.generate_email(),
        "password": Generators.generate_password(8)
    }