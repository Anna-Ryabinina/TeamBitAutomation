from src.locators import *
from selene.api import *
from src.pages_url import *
import time


class LoginPage(object):

    def __init__(self):
        self.email_input = s(by.xpath(SIGNIN_EMAIL_TEXT_INPUT))
        self.password_input = s(by.xpath(SIGNIN_PASSWORD_TEXT_INPUT))
        self.login_button = s(by.xpath(SIGNIN_BUTTON))
        self.login_with_google_button = s(by.xpath(SIGNIN_WITH_GOOGLE_BUTTON))
        self.login_with_slack_button = s(by.xpath(SIGNIN_WITH_SLACK_BUTTON))
        self.email_error_message = s(by.xpath(SIGNUP_EMAIL_ERROR_TEXT))
        self.password_error_message = s(by.xpath(SIGNIN_PASSWORD_ERROR_TEXT))
        self.forgot_link = s(by.xpath(SIGNIN_FORGOT_LINK))
        self.signup_for_free_link = s(by.xpath(SIGNUP_FOR_FREE_LINK))

    def login(self, email, password):
        self.email_input.set(email)
        self.password_input.set(password)
        self.login_button.click()
        return LoginPage()

    def login_as_user(self, user):
        self.email_input.set(user.email)
        self.password_input.set(user.password)
        self.login_button.click()
        return LoginPage()

    def open(self):
        browser.open_url(LOGIN_PAGE_URL)
        time.sleep(0.5)
        return LoginPage()


