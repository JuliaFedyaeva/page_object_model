from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser, MainPageLocators.MAIN_PAGE_LINK)
