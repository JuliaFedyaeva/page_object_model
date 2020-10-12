import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="None",
                     help="Choose your language")
    parser.addoption('--browser', action='store', default="None",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request, timeout=10):
    browser_language = request.config.getoption("language")
    if browser_language is None: raise pytest.UsageError('test run should contain language fo test')

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})

    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", browser_language)

    document = None

    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        document = webdriver.Chrome(options=options)
        document.implicitly_wait(5)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        document = webdriver.Firefox(firefox_profile=fp)
        document.implicitly_wait(5)
    else:
        print("Browser {} still is not implemented".format(browser_name))

    document.implicitly_wait(timeout)

    yield document
    print("\nquit document..")
    document.quit()
