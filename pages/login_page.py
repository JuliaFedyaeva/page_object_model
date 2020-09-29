from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser, LoginPageLocators.LOGIN_PAGE_LINK)

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, \
            "Login page is not opened"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTHORIZATION_FORM_EMAIL), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_EMAIL), \
            "Register form is not presented"

    def should_be_success_register_icon(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REGISTRATION_ICON), \
            "There is no success register icon on page"

    def should_be_success_register_message(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REGISTRATION_MESSAGE), \
            "There is no success registration message"
