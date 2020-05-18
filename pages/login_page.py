from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login pass field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS), "Register pass field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASS), "Reg confirm field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"
        assert True

