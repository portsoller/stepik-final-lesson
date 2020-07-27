from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form > button")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button55")