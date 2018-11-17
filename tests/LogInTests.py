import unittest
from selene.api import *
from src.pages_url import *
from tests.BaseTest import BaseTest
from src.pages.pages.LogInPage import LoginPage
from src.pages.pages.FeedbackPage import FeedbackPage
from src.test_data_generators.User import User
from src.test_data import *


class LoginTests(BaseTest):

    def test_sign_in_with_email(self):
        user = User(user_1)
        LoginPage().open().login(user.email, user.password)
        FeedbackPage().logo.should(be.visible)
        assert FEEDBACK_ALL_URL in browser.driver().current_url

    def test_sign_in_with_invalid_credentials(self):
        user = User(user_1)
        LoginPage().open().login(" ", user.password).email_error_message.should(be.visible)
        LoginPage().login(user.email, " ").password_error_message.should(be.visible)
        LoginPage().login(user.email, "1111").password_error_message.should(be.visible)

    def test_sign_in_with_google(self):
        LoginPage().open().login_with_google_button.click()
        assert 'accounts.google.com' in browser.driver().current_url, 'There vas not redirect to account.google.com'

    def test_sign_in_with_slack(self):
        LoginPage().open().login_with_slack_button.click()
        assert 'slack.com' in browser.driver().current_url, 'There was not redirect to slack.com'

    def test_go_to_sign_up_page(self):
        LoginPage().open().signup_for_free_link.click()
        assert SIGNUP_PAGE_URL in browser.driver().current_url, "There was not redirect to signup page"


if __name__ == '__main__':
    unittest.main()
