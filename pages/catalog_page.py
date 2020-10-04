from .base_page import BasePage
from .locators import CatalogPageLocators


class CatalogPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser, CatalogPageLocators.CATALOG_PAGE_LINK)

    def should_be_catalog_page(self):
        current_url = self.browser.current_url
        assert 'catalogue' in current_url, \
            "Catalog page is not opened"

    def find_first_item_name(self):
        return self.browser.find_element(*CatalogPageLocators.FIRST_ITEM_ON_CATALOG_NAME).text

    def add_product_to_cart(self):
        return self.browser.find_element(*CatalogPageLocators.BUTTON_ADD_TO_CART).click()
