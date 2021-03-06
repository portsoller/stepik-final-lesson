from pages.main_page import MainPage
from pages.product_page import ItemPage
from pages.login_page import LoginPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.add_product_to_the_basket()
    page.go_to_alert()