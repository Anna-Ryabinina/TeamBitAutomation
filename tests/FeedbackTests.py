import datetime
import unittest
import requests
import time
from selene.api import *
from src.test_data import *
from src.pages_url import *
from src.api_helpers.Authorisation import Authorisation
from src.api_helpers.ApiMethods import ApiMethods
from src.test_data_generators.User import User
from src.test_data_generators.Team import Team
from src.test_data_generators.Feedback_payload import FeedbackPayload
from src.pages.FeedbackPage import *
from src.pages.LogInPage import LoginPage
from src.pages.FeedbackRequestPopup import FeedbackRequestPopup

from tests.BaseTest import BaseTest


class FeedbackTests(BaseTest):

    def test_feedback_form_opens_from_feedback_page(self):
        user1 = User(user_1)
        user2 = User(user_2)
        LoginPage().open().login(user1.email, user1.password)
        (FeedbackPage()
         .send_feedback_button.click())
        (FeedbackRequestPopup()
         .popup.should(be.visible))
        (FeedbackRequestPopup()
         .send_feedback_button.should_not(be.enabled))
        (FeedbackRequestPopup()
         .add_value()
         .value_added.should(be.visible))
        (FeedbackRequestPopup()
         .add_template_to_feedback()
         .text_input.should_not(be.empty))
        (FeedbackRequestPopup()
         .type_recipient(user2.full_name)
         .recepient_added.should(be.visible))
        (FeedbackRequestPopup()
         .make_public()
         .send_button.should(have.text('public')))
        (FeedbackRequestPopup()
         .make_private()
         .send_button.should(have.text('private')))
        (FeedbackRequestPopup()
         .text_input.send_keys('test'))
        (FeedbackRequestPopup()
         .send_feedback_button.should(be.enabled))
        (FeedbackRequestPopup()
         .close()
         .popup.should_not(be.visible))


    def test_feedback_form_openes_from_sidebar(self):
        assert True


    def test_user_can_send_private_feedback_to_user(self):
        D = datetime.date.today().strftime('%b %d')
        user1 = User(user_1)
        user2 = User(user_2)
        LoginPage().open().login(user1.email, user1.password)
        FeedbackPage().send_feedback_button.click()
        (FeedbackRequestPopup()
         .type_recipient(user2.full_name)
         .add_value()
         .add_template_to_feedback()
         .add_text(D + 'test_user_can_send_private_feedback_to_user')
         .click_send_feedback_button())
        fb = FeedbackPage().open_sent().get_feedback_by_text(D + 'test_user_can_send_private_feedback_to_user')
        assert fb is not None
        fb.value.should(be.visible)
        fb.people.should(have.text('firstname1'))
        fb.people.should(have.text('firstname2'))
        fb.to_praise_link.should(have.text('Add to praise'))
        fb.flag_link.should(have.text('Flag for follow-up'))
        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(D + 'test_user_can_send_private_feedback_to_user')
        assert fb is None

    def test_user_can_send_public_feedback_to_team(self):
        D = datetime.date.today().strftime('%b %d')
        user = User(user_1)
        team = Team(team_34)
        LoginPage().open().login(user.email, user.password)
        FeedbackPage().send_feedback_button.click()
        (FeedbackRequestPopup()
         .type_recipient(team.name)
         .make_public()
         .add_text(D + 'test_user_can_send_public_feedback_to_team')
         .click_send_feedback_button())
        fb = FeedbackPage().open_sent().get_feedback_by_text(D + 'test_user_can_send_public_feedback_to_team')
        assert fb is not None
        fb.people.should(have.text('firstname1'))
        fb.people.should(have.text('team'))
        fb.to_praise_link.should(have.text('Added to praise'))
        fb = FeedbackPage().open_sent().get_feedback_by_text(D + 'test_user_can_send_public_feedback_to_team')
        assert fb is not None

    def test_user_can_add_sent_feedback_to_praise(self):
        user1 = User(user_1)
        user2 = User(user_2)
        payload = FeedbackPayload([user2]).generate_feedback_data()
        sess = requests.session()
        Authorisation(sess).login_with_email(user1)
        ApiMethods(sess).send_feedback(payload.json)
        sess.close()
        LoginPage().open().login(user1.email, user1.password)
        time.sleep(0.5)
        browser.open_url(FEEDBACK_SENT_URL)
        fb = FeedbackPage().get_feedback_by_text(payload.text)
        assert fb is not None
        fb.to_praise_link.click()
        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(payload.text)
        assert fb is not None
        fb.to_praise_link.click()
        browser.driver().refresh()
        fb = FeedbackPage().get_feedback_by_text(payload.text)
        assert fb is None

    def test_user_can_add_recieved_feedback_to_praise(self):
        user1 = User(user_1)
        user2 = User(user_2)
        payload = FeedbackPayload([user1]).generate_feedback_data()
        sess = requests.session()
        Authorisation(sess).login_with_email(user2)
        ApiMethods(sess).send_feedback(payload.json)
        sess.close()
        LoginPage().open().login(user1.email, user1.password)
        time.sleep(0.5)
        fb = FeedbackPage().open_sent().get_feedback_by_text(payload.text)
        fb.to_praise_link.click()
        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(payload.text)
        assert fb is not None
        fb.to_praise_link.click()
        browser.driver().refresh()
        fb = FeedbackPage().get_feedback_by_text(payload.text)
        assert fb is None

    def test_user_can_mark_sent_feedback_with_flag(self):
        user1 = User(user_1)
        user3 = User(user_3)
        payload = FeedbackPayload([user3], shared=True).generate_feedback_data()
        sess = requests.session()
        Authorisation(sess).login_with_email(user1)
        ApiMethods(sess).send_feedback(payload.json)
        sess.close()
        LoginPage().open().login(user1.email, user1.password)
        time.sleep(0.5)
        fb = FeedbackPage().open_sent().get_feedback_by_text(payload.text)
        fb.flag_link.click()
        fb = FeedbackPage().open_flagged().get_feedback_by_text(payload.text)
        assert fb is not None
        fb.flag_link.click()
        browser.driver().refresh()
        fb = FeedbackPage().get_feedback_by_text(payload.text)
        assert fb is None

    def test_user_can_mark_recieved_feedback_with_flag(self):
        user1 = User(user_1)
        user3 = User(user_3)
        payload = FeedbackPayload([user1], shared=True).generate_feedback_data()
        sess = requests.session()
        Authorisation(sess).login_with_email(user3)
        ApiMethods(sess).send_feedback(payload.json)
        sess.close()
        LoginPage().open().login(user1.email, user1.password)
        time.sleep(0.5)
        fb = FeedbackPage().open_sent().get_feedback_by_text(payload.text)
        fb.flag_link.click()
        fb = FeedbackPage().open_flagged().get_feedback_by_text(payload.text)
        assert fb is not None
        fb.flag_link.click()
        browser.driver().refresh()
        fb = FeedbackPage().get_feedback_by_text(payload.text)
        assert fb is None


if __name__ == '__main__':
    unittest.main()
