from .pages.login_page import LoginPage
import pytest


@pytest.mark.user
class TestPassword():
    def test_user_can_remind_password(self, browser):
        # Arrange
        page = LoginPage(browser)
        page.open()
        page.should_be_remind_password_link()
        # Steps
        page.click_to_remind_password_link()
        page.should_be_remind_password_form()
        page.reset_password()
        # Arrange
        page.should_be_success_message_about_reset_password()
