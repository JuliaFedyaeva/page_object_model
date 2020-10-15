from .pages.cart_page import CartPage
from .pages.catalog_page import CatalogPage
from .pages.login_page import LoginPage
from .pages.data import LoginPageData
from .pages.checkout_page import CheckoutPage
import pytest


@pytest.fixture(scope="function")
def setup(browser):
    page = LoginPage(browser)
    page.open()
    page.should_be_login_page()
    page.authorize_user(LoginPageData.EMAIL_AUTH, LoginPageData.PASSWORD)
    page.should_be_success_register_or_auth_message()
    page.go_to_catalog_page()
    page_catalog = CatalogPage(browser)
    page_catalog.should_be_catalog_page()
    page_catalog.add_product_to_cart()
    page_catalog.go_to_cart()
    page_cart = CartPage(browser)
    page_cart.should_be_no_empty_cart()
    page_cart.go_to_buy_process()
    yield browser


class TestBuyProduct():
    def test_user_can_buy_product(self, setup):
        # Arrange
        page_checkout = CheckoutPage(setup)
        page_checkout.should_be_checkout_page()
        page_checkout.should_be_address_form()
        # Steps
        page_checkout.set_shipping_address()
        page_checkout.go_to_payment_page()
        # page_checkout.set_payment_information()
        page_checkout.go_to_preview_order()
        page_checkout.should_be_preview_order_page()
        page_checkout.go_to_place_order()
        # Assert
        page_checkout.should_be_success_message_order()

    @pytest.mark.xfail
    def test_user_cant_buy_product_without_payment(self, setup):
        # Arrange
        page_checkout = CheckoutPage(setup)
        page_checkout.should_be_checkout_page()
        page_checkout.should_be_address_form()
        # Steps
        page_checkout.set_shipping_address()
        page_checkout.go_to_payment_page()
        # page_checkout.payment_information_is_empty()
        # Assert
        page_checkout.should_be_disabled_button_to_preview()
        page_checkout.go_to_preview_order()
