from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_TITLE = (By.XPATH, "//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")