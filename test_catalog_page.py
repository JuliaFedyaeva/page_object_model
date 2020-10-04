from .pages.catalog_page import CatalogPage
from .pages.cart_page import CartPage


def test_guest_user_can_add_product_to_cart(browser):
    page = CatalogPage(browser)
    page.open()
    page.should_be_catalog_page()
    item_name = page.find_first_item_name()
    page.add_product_to_cart()
    page.should_be_cart_link()
    page.go_to_cart()
    page_cart = CartPage(browser)
    item_in_cart = page_cart.item_in_cart()
    assert item_name == item_in_cart, \
        "No or wrong item in the cart"
