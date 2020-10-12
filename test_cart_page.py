from .pages.cart_page import CartPage
from .pages.catalog_page import CatalogPage
from .pages.login_page import LoginPage
from .pages.data import LoginPageData


class TestBuyProduct():
    def test_user_can_buy_product(self, browser):
        # Arrange
        page = LoginPage(browser)
        page.open()
        page.should_be_login_page()
        page.authorizate_user(LoginPageData.EMAIL_AUTH, LoginPageData.PASSWORD)
        page.should_be_success_register_or_auth_message()
        page.go_to_catalog_page()
        page = CatalogPage(browser)
        page.should_be_catalog_page()
        page.add_product_to_cart()
        #Steps
        page.go_to_cart()
        page_cart = CartPage(browser)
        page_cart.should_be_no_empty_cart()

        #Assert



