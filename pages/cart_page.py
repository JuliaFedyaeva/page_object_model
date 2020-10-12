from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser, CartPageLocators.CART_PAGE_LINK)

    def item_in_cart(self):
        return self.browser.find_element(*CartPageLocators.ITEM_IN_CART).text

    def should_be_no_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.ITEM_IN_CART), \
            "Cart is empty"

    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.ITEM_IN_CART), \
            "Cart is not empty"
