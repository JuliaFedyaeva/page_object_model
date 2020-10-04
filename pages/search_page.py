from .base_page import BasePage
from .locators import SearchPageLocators
from .data import SearchOnMainPageData


class SearchPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser, SearchPageLocators.SEARCH_PAGE_LINK)

    def should_be_right_item_after_search_from_main_page(self):
        self.is_element_present(*SearchPageLocators.SEARCH_ITEM_LOCATOR)

        book_name_on_page = self.browser.find_element(*SearchPageLocators.SEARCH_ITEM_LOCATOR).text
        book_name = SearchOnMainPageData.BOOK_NAME
        assert book_name in book_name_on_page, \
            "Search item '%s' should contain text '%s'" % (book_name_on_page, book_name)
