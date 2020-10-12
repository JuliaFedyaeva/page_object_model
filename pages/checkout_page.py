from .base_page import BasePage
from .locators import CheckoutPageLocators
from .data import CheckoutPageData
from selenium.webdriver.support.ui import Select


class CheckoutPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser, CheckoutPageLocators.CHECKOUT_PAGE_LINK)

    def should_be_checkout_page(self):
        current_url = self.browser.current_url
        assert 'checkout' in current_url, \
            "Checkout page is not opened"

    def set_shipping_address(self):
        self.browser.find_element(*CheckoutPageLocators.INPUT_NAME).send_keys(CheckoutPageData.NAME)
        self.browser.find_element(*CheckoutPageLocators.INPUT_LASTNAME).send_keys(CheckoutPageData.LASTNAME)
        self.browser.find_element(*CheckoutPageLocators.INPUT_ADDRESS).send_keys(CheckoutPageData.ADDRESS)
        self.browser.find_element(*CheckoutPageLocators.INPUT_CITY).send_keys(CheckoutPageData.CITY)
        self.browser.find_element(*CheckoutPageLocators.INPUT_POSTCODE).send_keys(CheckoutPageData.POSTCODE)
        select = Select(self.browser.find_element(*CheckoutPageLocators.SELECT_COUNTRY))
        select.select_by_value(CheckoutPageData.COUNTRY)

    def go_to_payment_page(self):
        return self.browser.find_element(*CheckoutPageLocators.BUTTON_TO_CONTINUE).click()

    def go_to_payment_page_if_address_already_present(self):
        return self.browser.find_element(*CheckoutPageLocators.BUTTON_TO_CONTINUE_WITH_SAVED_ADDRESS).click()

    def should_be_address_form(self):
        self.is_element_present(*CheckoutPageLocators.INPUT_NAME)
        self.is_element_present(*CheckoutPageLocators.INPUT_ADDRESS)

    def go_to_preview_order(self):
        return self.browser.find_element(*CheckoutPageLocators.BUTTON_TO_PREVIEW_ORDER).click()

    def should_be_preview_order_page(self):
        current_url = self.browser.current_url
        assert 'checkout/preview' in current_url, \
            "Preview order page is not opened"

    def go_to_place_order(self):
        return self.browser.find_element(*CheckoutPageLocators.BUTTON_TO_PLACE_ORDER).click()

    def should_be_success_message_order(self):
        assert self.is_element_present(*CheckoutPageLocators.SUCCESS_ORDER_MESSAGE_NUM)
        order_num = self.browser.find_element(*CheckoutPageLocators.ORDER_NUM_MESSAGE).text
        order_num_in_message = self.browser.find_element(*CheckoutPageLocators.SUCCESS_ORDER_MESSAGE_NUM).text
        assert order_num_in_message in order_num, \
            "Unsuccessful try to place order"

    def should_be_disabled_button_to_preview(self):
        assert self.is_element_present(*CheckoutPageLocators.BUTTON_TO_PREVIEW_ORDER)
        button = self.browser.find_element(*CheckoutPageLocators.BUTTON_TO_PREVIEW_ORDER)
        assert button.get_attribute('disabled') is not None, \
            "No disabled button on payment page"
