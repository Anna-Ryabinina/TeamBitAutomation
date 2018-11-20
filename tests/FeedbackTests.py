import unittest
import requests
import time

from src.test_data import *
from src.api_helpers.ApiMethods import ApiMethods
from src.test_data_generators.User import User
from src.test_data_generators.Team import Team
from src.test_data_generators.FeedbackPayload import FeedbackPayload
from src.pageobjects.pages.FeedbackPage import *
from src.pageobjects.pages.LogInPage import LoginPage
from src.pageobjects.popups.FeedbackRequestPopup import FeedbackRequestPopup

from tests.BaseTest import BaseTest


class FeedbackTests(BaseTest):

    def test_user_can_send_private_feedback_to_user(self):

        user1 = User(user_1)
        user2 = User(user_2)
        feedback_text = self.execute_date + 'test_user_can_send_private_feedback_to_user'

        LoginPage().open().login(user1.email, user1.password)

        FeedbackPage().send_feedback_button.click()

        (FeedbackRequestPopup()
         .type_recipient(user2.full_name)
         .add_value()
         .add_template_to_feedback()
         .add_text(feedback_text)
         .click_send_feedback_button())

        fb = FeedbackPage().open_sent().get_feedback_by_text(feedback_text)

        assert fb is not None

        fb.value.should(be.visible)
        fb.people.should(have.text('firstname1'))
        fb.people.should(have.text('firstname2'))
        fb.to_praise_link.should(have.text('Add to praise'))
        fb.flag_link.should(have.text('Flag for follow-up'))

        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(feedback_text)

        assert fb is None

    def test_user_can_send_public_feedback_to_team(self):

        user = User(user_1)
        team = Team(team_34)
        feedback_text = self.execute_date + 'test_user_can_send_public_feedback_to_team'

        LoginPage().open().login(user.email, user.password)

        FeedbackPage().send_feedback_button.click()

        (FeedbackRequestPopup()
         .type_recipient(team.name)
         .make_public()
         .add_text(feedback_text)
         .click_send_feedback_button())

        fb = FeedbackPage().open_sent().get_feedback_by_text(feedback_text)
        assert fb is not None

        fb.people.should(have.text('firstname1'))
        fb.people.should(have.text('team'))
        fb.to_praise_link.should(have.text('Added to praise'))

        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(feedback_text)
        assert fb is not None

    def test_user_can_add_sent_feedback_to_praise(self):
        user1 = User(user_1)
        user2 = User(user_2)
        payload = FeedbackPayload([user2], text_prefix=self.execute_date).generate_feedback_data()
        sess = requests.session()

        ApiMethods(sess).login_as_user(user1)
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
        payload = FeedbackPayload([user1], text_prefix=self.execute_date).generate_feedback_data()
        sess = requests.session()

        ApiMethods(sess).login_as_user(user2)
        ApiMethods(sess).send_feedback(payload.json)
        sess.close()

        LoginPage().open().login(user1.email, user1.password)
        time.sleep(0.5)

        fb = FeedbackPage().get_feedback_by_text(payload.text)
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
        payload = FeedbackPayload([user3], text_prefix=self.execute_date, shared=True).generate_feedback_data()
        sess = requests.session()

        ApiMethods(sess).login_as_user(user1)
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
        payload = FeedbackPayload([user1], text_prefix =self.execute_date, shared=True).generate_feedback_data()
        sess = requests.session()

        ApiMethods(sess).login_as_user(user3)
        ApiMethods(sess).send_feedback(payload.json)
        sess.close()

        LoginPage().open().login(user1.email, user1.password)
        time.sleep(0.5)

        fb = FeedbackPage().get_feedback_by_text(payload.text)
        fb.flag_link.click()
        fb = FeedbackPage().open_flagged().get_feedback_by_text(payload.text)
        assert fb is not None

        fb.flag_link.click()
        browser.driver().refresh()
        fb = FeedbackPage().get_feedback_by_text(payload.text)
        assert fb is None


if __name__ == '__main__':
    unittest.main()
