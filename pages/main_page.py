from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def add_product_to_the_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def go_to_alert(self):
        alert = self.browser.switch_

