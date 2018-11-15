from selene.api import *
from src.locators import *
from src.pages_url import *


class SignUpPage(object):
    def __init__(self):
        self.email_input = s(by.xpath(SIGNUP_EMAIL_TEXT_INPUT))
        self.signup_button = s(SIGNUP_BUTTON)
        self.signup_with_google_button = s(by.xpath(SIGNUP_WITH_GOOGLE_BUTTON))
        self.signup_with_slack_button = s(by.xpath(SIGNUP_WITH_SLACK_BUTTON))
        self.signin_here_link = s(by.xpath(SIGNIN_HERE_LINK))
        self.email_error_message = s(by.xpath(SIGNUP_EMAIL_ERROR_TEXT))

    def signup(self, email):
        self.email_input.set(email)
        self.signup_button.click()
        return SignUpPage()

    def open(self):
        browser.open_url(SIGNUP_PAGE_URL)
        return SignUpPage()