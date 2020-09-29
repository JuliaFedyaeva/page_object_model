from .pages.product_page import ProductPage
import pytest
from .pages.cart_page import CartPage


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser)
    page.open()
    page.should_be_no_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_product_to_cart()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(browser)
    cart_page.should_be_empty_cart()


class TestUserAddToBasketFromProductPage():
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser)
        page.open()
        page.add_product_to_cart()
        page.should_be_no_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser)
        page.open()
        page.add_product_to_cart()
        page.should_be_right_item_in_success_message()
        page.should_be_right_total_price_in_success_message()


