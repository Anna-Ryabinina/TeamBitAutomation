import unittest
import time
from selene.api import *
from src.pages_url import *

from tests.BaseTest import BaseTest
from src.pages.pages.SignUpPage import SignUpPage
from src.pages.popups.OnboardingPopup import OnboardingPopup


class SignUpTests(BaseTest):

    def test_sign_up_with_email(self):
        test_email = 'autotest' + str(time.time()) + '@test.com'
        SignUpPage().open().signup(test_email)
        OnboardingPopup().popup.should(be.existing).should(be.visible)

    def test_sign_up_empty_email(self):
        SignUpPage().open().signup('').email_error_message.should(be.visible)


    def test_sign_up_with_google(self):
        SignUpPage().open().signup_with_google_button.click()
        assert "google" in browser.driver().current_url
        #"There was not redirect to account.google.com"

    def test_sign_up_with_slack(self):
        SignUpPage().open().signup_with_slack_button.click()
        assert "slack" in browser.driver().current_url
        #"There was not redirect to slack.com"

    def test_go_to_sign_in_page(self):
        SignUpPage().open().signin_here_link.click()
        assert LOGIN_PAGE_URL in browser.driver().current_url
        #"There was not redirect to signin page"


if __name__ == '__main__':
    unittest.main()
