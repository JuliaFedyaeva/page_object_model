import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
from .pages.data import LoginPageData
from .pages.search_page import SearchPage


@pytest.mark.login
@pytest.mark.guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()
        # Steps
        page.go_to_login_page()
        login_page = LoginPage(browser)
        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()
        # Steps
        page.should_be_login_link()


@pytest.mark.guest
class TestCanSeeOnMainPage():
    def test_guest_cant_see_product_in_basket_without_add(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()
        page.go_to_cart()
        cart_page = CartPage(browser)
        # Assert
        cart_page.should_be_empty_cart()

    def test_guest_can_see_catalog_page(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()
        # Assert
        page.should_be_catalog_link()


@pytest.mark.guest
class TestCanRegisterFromMainPage():
    def test_guest_can_register(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.should_be_register_form()
        # Steps
        login_page.register_new_user(LoginPageData.EMAIL, LoginPageData.PASSWORD)
        # Assert
        login_page.should_be_success_register_or_auth_message()
        login_page.should_be_success_register_or_auth_icon()


@pytest.mark.user
class TestCanAuthFromMainPage():
    def test_user_can_authorizate(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.should_be_authorization_form()
        # Steps
        login_page.authorizate_user(LoginPageData.EMAIL_AUTH, LoginPageData.PASSWORD)
        # Assert
        login_page.should_be_success_register_or_auth_icon()
        login_page.should_be_success_register_or_auth_message()


@pytest.mark.user
class TestCanSearchFromMainPage():
    def test_user_can_search_book(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()
        page.should_be_search_form()
        # Steps
        page.search_item()
        search_page = SearchPage(browser)
        # Assert
        search_page.should_be_right_item_after_search_from_main_page()
