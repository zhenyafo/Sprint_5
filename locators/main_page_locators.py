from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет")
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    TOPPINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_TAB = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")
      