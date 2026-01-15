from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.education-services.ru/"
    
    def open(self, url=""):
        if url:
            self.driver.get(f"{self.base_url}{url}")
        else:
            self.driver.get(self.base_url)
    
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()
    
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def is_element_present(self, locator, timeout=5):
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False