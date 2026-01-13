import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from generators.data_generator import DataGenerator


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def data_generator():
    return DataGenerator()


@pytest.fixture
def test_user_data():
    return {
        "email": "test-user-example@yandex.ru",
        "password": "Password123",
        "name": "Тестовый Пользователь"
    }
