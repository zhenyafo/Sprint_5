from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_TITLE = (By.LINK_TEXT, "Профиль")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
     