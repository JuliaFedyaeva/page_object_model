import time


def get_new_email():
    return str(time.time()) + "@fakemail.org"


class LoginPageData():
    EMAIL = get_new_email()
    EMAIL_AUTH = 'its_me@mail.ru'
    PASSWORD = "nekakuvseh123"


class SearchOnMainPageData():
    BOOK_NAME = 'Google Hacking'
