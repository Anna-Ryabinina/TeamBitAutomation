import datetime
import unittest
import time
import requests
from selene.api import *
from src.pages_url import *
from src.test_data import *
from src.test_data_generators.User import User
from src.test_data_generators.RequestPayload import RequestPayload
from src.api_helpers.ApiMethods import ApiMethods
from src.api_helpers.Authorisation import Authorisation
from src.pages.LogInPage import LoginPage
from src.pages.RequestPage import RequestsPage
from src.pages.FeedbackRequestPopup import FeedbackRequestPopup
from src.pages.FeedbackPage import FeedbackPage
from tests.BaseTest import BaseTest


class MyTestCase(BaseTest):

    def test_user_can_send_request(self):
        D = datetime.date.today().strftime('%b %d')
        user1 = User(user_1)
        user2 = User(user_2)
        (LoginPage()
         .open()
         .login(user1.email, user1.password))
        time.sleep(1)
        browser.open_url(REQUEST_PAGE_URL)
        RequestsPage().request_feedback_button.click()
        (FeedbackRequestPopup()
         .type_recipient(user2.full_name)
         .type_text(D + 'test_user_can_send_request')
         .click_send_request_button())
        RequestsPage().open()
        rq = RequestsPage().get_request_by_text(D + 'test_user_can_send_request')
        assert rq is not None

    def test_user_receive_request(self):
        D = datetime.date.today().strftime('%b %d')
        user1 = User(user_1)
        user2 = User(user_2)
        sess = requests.session()
        Authorisation(sess).login_with_email(user2)
        (ApiMethods(sess)
         .send_request(RequestPayload([user1], D + 'test_user_receive_request')
                       .generate_request_data()))
        sess.close()
        (LoginPage()
         .open()
         .login(user1.email, user1.password))
        time.sleep(1)
        rq = RequestsPage().open().get_request_by_text(D + 'test_user_receive_request')
        assert rq is not None
        rq.dismiss_link.should(be.visible)
        rq.send_feedback_button.should(be.visible)
        rq.send_feedback_button.should(be.enabled)

    def test_user_can_dismiss_request(self):
        D = datetime.date.today().strftime('%b %d')
        user1 = User(user_1)
        user2 = User(user_2)
        sess = requests.session()
        Authorisation(sess).login_with_email(user2)
        (ApiMethods(sess)
         .send_request(RequestPayload([user1], D + 'test_user_can_dismiss_request')
                       .generate_request_data()))
        sess.close()
        (LoginPage()
         .open()
         .login(user1.email, user1.password))
        time.sleep(1)
        rq = RequestsPage().open().get_request_by_text(D + 'test_user_can_dismiss_request')
        rq.dismiss_link.click()
        rq = RequestsPage().open().get_request_by_text(D + 'test_user_can_dismiss_request')
        assert rq is None

    def test_user_can_resolve_request(self):
        D = datetime.date.today().strftime('%b %d')
        user1 = User(user_1)
        user2 = User(user_2)
        sess = requests.session()
        Authorisation(sess).login_with_email(user2)
        (ApiMethods(sess)
         .send_request(RequestPayload([user1], D + 'test_user_can_dismiss_request')
                       .generate_request_data()))
        sess.close()
        (LoginPage()
         .open()
         .login(user1.email, user1.password))
        time.sleep(1)
        rq = RequestsPage().open().get_request_by_text(D + 'test_user_can_dismiss_request')
        rq.send_feedback_button.click()
        FeedbackRequestPopup().popup.should(be.visible)
        (FeedbackRequestPopup()
         .type_text(D + 'test_user_can_resolve_request')
         .click_send_feedback_button())
        fb = FeedbackPage().open_sent().get_feedback_by_text(D + 'test_user_can_resolve_request')
        assert fb is not None


if __name__ == '__main__':
    unittest.main()
