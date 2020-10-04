from .pages.login_page import LoginPage


def test_user_can_remind_password(browser):
    page = LoginPage(browser)
    page.open()
    page.should_be_remind_password_link()
    page.click_to_remind_password_link()
    page.should_be_remind_password_form()
    page.reset_password()
    page.should_be_success_message_about_reset_password()

