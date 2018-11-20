import unittest
import time
import requests
from selene.api import *
from src.pages_url import *
from src.test_data import *
from src.test_data_generators.User import User
from src.test_data_generators.RequestPayload import RequestPayload
from src.api_helpers.ApiMethods import ApiMethods
from src.pageobjects.pages.LogInPage import LoginPage
from src.pageobjects.pages.RequestPage import RequestsPage
from src.pageobjects.popups.FeedbackRequestPopup import FeedbackRequestPopup
from src.pageobjects.pages.FeedbackPage import FeedbackPage
from tests.BaseTest import BaseTest


class RequestTests(BaseTest):

    def test_user_can_send_request(self):
        request_text = self.execute_date + 'test_user_can_send_request'
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
         .type_text(request_text)
         .click_send_request_button())

        RequestsPage().open()
        rq = RequestsPage().open_sent().get_request_by_text(request_text)
        assert rq is not None

    def test_user_receive_request(self):
        request_text = self.execute_date + 'test_user_receive_request'
        user1 = User(user_1)
        user2 = User(user_2)
        sess = requests.session()

        ApiMethods(sess).login_as_user(user2)
        request_payload = RequestPayload([user1], text=request_text).generate_request_data()

        (ApiMethods(sess)
         .send_request(request_payload.json))
        sess.close()

        (LoginPage()
         .open()
         .login(user1.email, user1.password))

        time.sleep(1)
        rq = RequestsPage().open().get_request_by_text(request_text)
        assert rq is not None
        rq.dismiss_link.should(be.visible)
        rq.send_feedback_button.should(be.visible)
        rq.send_feedback_button.should(be.enabled)

    def test_user_can_dismiss_request(self):
        request_text = self.execute_date + 'test_user_can_dismiss_request'
        user1 = User(user_1)
        user2 = User(user_2)

        sess = requests.session()
        ApiMethods(sess).login_as_user(user2)
        request_payload = RequestPayload([user1], text=request_text).generate_request_data()

        (ApiMethods(sess)
         .send_request(request_payload.json))
        sess.close()

        (LoginPage()
         .open()
         .login(user1.email, user1.password))
        time.sleep(1)

        rq = RequestsPage().open().get_request_by_text(request_text)
        rq.dismiss_link.click()
        rq = RequestsPage().open().get_request_by_text(request_text)
        assert rq is None

    def test_user_can_resolve_request(self):
        user1 = User(user_1)
        user2 = User(user_2)
        request_text = self.execute_date + 'test_user_can_dismiss_request'
        sess = requests.session()

        ApiMethods(sess).login_as_user(user2)
        request_payload = RequestPayload([user1], text=request_text).generate_request_data()

        (ApiMethods(sess)
         .send_request(request_payload.json))
        sess.close()

        (LoginPage()
         .open()
         .login(user1.email, user1.password))
        time.sleep(1)

        rq = RequestsPage().open().get_request_by_text(request_text)
        rq.send_feedback_button.click()

        FeedbackRequestPopup().popup.should(be.visible)

        (FeedbackRequestPopup()
         .type_text(request_text)
         .click_send_feedback_button())

        fb = FeedbackPage().open_sent().get_feedback_by_text(request_text)
        assert fb is not None


if __name__ == '__main__':
    unittest.main()
