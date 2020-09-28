from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration - password1')
    REGISTRATION_FORM_PASSWORD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')

    AUTHORIZATION_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    AUTHORIZATION_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')

