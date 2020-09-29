import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
from .pages.data import LoginPageData


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_cart()
        cart_page = CartPage(browser)
        cart_page.should_be_empty_cart()

    def test_guest_can_register(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.should_be_register_form()
        login_page.register_new_user(LoginPageData.EMAIL, LoginPageData.PASSWORD)
        login_page.should_be_success_register_message()
        login_page.should_be_success_register_icon()
