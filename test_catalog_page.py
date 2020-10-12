from .pages.catalog_page import CatalogPage
from .pages.cart_page import CartPage
import pytest


@pytest.mark.guest
class TestActionsWithProduct():
    def test_guest_user_can_add_product_to_cart(self, browser):
        # Arrange
        page = CatalogPage(browser)
        page.open()
        page.should_be_catalog_page()
        item_name = page.find_first_item_name()
        # Steps
        page.add_product_to_cart()
        page.should_be_cart_link()
        page.go_to_cart()
        page_cart = CartPage(browser)
        item_in_cart = page_cart.item_in_cart()
        # Assert
        assert item_name == item_in_cart, \
            "No or wrong item in the cart"
