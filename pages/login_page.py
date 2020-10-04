from .base_page import BasePage
from .locators import LoginPageLocators
from .data import LoginPageData


class LoginPage(BasePage):
    def __init__(self, browser):
        BasePage.__init__(self, browser, LoginPageLocators.LOGIN_PAGE_LINK)

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_BUTTON).click()

    def authorizate_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.AUTHORIZATION_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.AUTHORIZATION_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.AUTHORIZATION_FORM_BUTTON).click()

    def click_to_remind_password_link(self):
        return self.browser.find_element(*LoginPageLocators.PASSWORD_RESET_LINK).click()

    def reset_password(self):
        self.browser.find_element(*LoginPageLocators.PASSWORD_RESET_EMAIL_INPUT).send_keys(LoginPageData.EMAIL_AUTH)
        self.browser.find_element(*LoginPageLocators.PASSWORD_RESET_BUTTON).click()

    def should_be_remind_password_link(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_RESET_LINK), \
            "There is no password reset link"

    def should_be_success_message_about_reset_password(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_MESSAGE_HEADER), \
            "Email wasn't sent, there is no heading about success sending"

    def should_be_remind_password_form(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_RESET_EMAIL_INPUT), \
            "There is no password reset email input"

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

    def should_be_authorization_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTHORIZATION_FORM_EMAIL), \
            "Register form is not presented"

    def should_be_success_register_or_auth_icon(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_SIGN_ICON), \
            "There is no success register/auth icon on page"

    def should_be_success_register_or_auth_message(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_REGISTRATION_MESSAGE), \
            "There is no success registration message"
