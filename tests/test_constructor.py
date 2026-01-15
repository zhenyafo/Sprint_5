import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from pages.main_page import MainPage


class TestConstructor:
    def test_switch_to_buns_tab(self, driver):
        main_page = MainPage(driver)
        
        main_page.open()
        
        main_page.click_sauces_section()
        main_page.click_buns_section()
        
        active_tab_text = main_page.get_active_tab_text()
        assert "Булки" in active_tab_text
    
    def test_switch_to_sauces_tab(self, driver):
        main_page = MainPage(driver)
        
        main_page.open()
        
        main_page.click_sauces_section()
        
        active_tab_text = main_page.get_active_tab_text()
        assert "Соусы" in active_tab_text
    
    def test_switch_to_toppings_tab(self, driver):
        main_page = MainPage(driver)
        
        main_page.open()
        
        main_page.click_toppings_section()
        
        active_tab_text = main_page.get_active_tab_text()
        assert "Начинки" in active_tab_text