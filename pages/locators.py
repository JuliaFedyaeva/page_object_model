from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_CART = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')

# class MainPageLocators():


class LoginPageLocators():
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration - password1')
    REGISTRATION_FORM_PASSWORD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')

    AUTHORIZATION_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    AUTHORIZATION_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')


class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, '#add_to_basket_form button.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRODUCT_IN_SUCCESS_ADD_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    TOTAL_PRICE_IN_SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')


class CartPageLocators():
    BUTTON_CHECKOUT = (By.PARTIAL_LINK_TEXT, 'checkout')
    ITEM_IN_CART = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[2]/h3/a')
