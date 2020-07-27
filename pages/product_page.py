from .base_page import BasePage
from .locators import ProductPageLocators


class ItemPage(BasePage):
    def should_be_product(self):
        self.should_be_product_url()
        self.should_be_product_page()

    def should_be_product_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/?promo=newYear" in self.browser.current_url, "URL of the login page is not correct"
        assert True

    def should_be_product_page(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"
        assert True
