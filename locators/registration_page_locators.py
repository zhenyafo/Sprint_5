from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.LINK_TEXT, "Войти")
    PASSWORD_ERROR = (By.CLASS_NAME, "input__error")