from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        link.click()

    def go_to_cart(self):
        view_link = self.browser.find_element(*ProductPageLocators.BUTTON_VIEW_CART)
        view_link.click()

    def get_name_item_from_success_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_IN_SUCCESS_ADD_MESSAGE).text

    def get_item_price_from_success_message(self):
        return self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_IN_SUCCESS_MESSAGE).text

    def get_item_name_on_product_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_item_price_on_product_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_right_item_in_success_message(self):
        assert self.get_item_name_on_product_page() == self.get_name_item_from_success_message(), \
            "Wrong item name in success add message"

    def should_be_right_total_price_in_success_message(self):
        assert self.get_item_price_on_product_page() == self.get_item_price_from_success_message(), \
            "Wrong total price in success add message"

    def should_be_no_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
