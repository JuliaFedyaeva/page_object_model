import time


def get_new_email():
    return str(time.time()) + "@fakemail.org"


class LoginPageData():
    EMAIL = get_new_email()
    PASSWORD = "nekakuvseh123"
