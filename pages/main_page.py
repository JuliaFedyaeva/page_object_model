from .base_page import BasePage
from .data import SearchOnMainPageData
from .locators import MainPageLocators
from .locators import BasePageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser, MainPageLocators.MAIN_PAGE_LINK)

    def set_input_search(self):
        self.browser.find_element(*BasePageLocators.INPUT_SEARCH).send_keys(SearchOnMainPageData.BOOK_NAME)
        self.browser.find_element(*BasePageLocators.INPUT_SEARCH_BUTTON).click()
