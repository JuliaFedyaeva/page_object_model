from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
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
