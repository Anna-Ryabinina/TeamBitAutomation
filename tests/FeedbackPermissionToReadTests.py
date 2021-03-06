import datetime
import unittest
import requests
from selenium import webdriver
from selene.api import *
from webdriver_manager.chrome import ChromeDriverManager

from tests.BaseTest import BaseTest
from src.pageobjects.pages.LogInPage import LoginPage
from src.pageobjects.pages.FeedbackPage import FeedbackPage
from src.api_helpers.ApiMethods import ApiMethods
from src.test_data_generators.FeedbackPayload import FeedbackPayload
from src.test_data_generators.User import User
from src.test_data_generators.Team import Team
from src.test_data import *
from src.pages_url import *


class FeedbackPermissionToRead(BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.execute_date = datetime.datetime.today().strftime('%c')
        cls.user1 = User(user_1)
        cls.user2 = User(user_2)
        cls.user3 = User(user_3)
        cls.team13 = Team(team_13)
        cls.team34 = Team(team_34)

        cls.fb1 = FeedbackPayload().generate_feedback_to_send([cls.user1], cls.execute_date)
        cls.fb2 = FeedbackPayload().generate_feedback_to_send([cls.user1], cls.execute_date, is_shared=True)
        cls.fb3 = FeedbackPayload().generate_feedback_to_send([cls.user3], cls.execute_date)
        cls.fb4 = FeedbackPayload().generate_feedback_to_send([cls.user3], cls.execute_date, is_shared=True)
        cls.fb5 = FeedbackPayload().generate_feedback_to_send([cls.team13], cls.execute_date)
        cls.fb6 = FeedbackPayload().generate_feedback_to_send([cls.team34], cls.execute_date)

        sess = requests.session()
        ApiMethods(sess).login_as_user(cls.user2)
        fb = ApiMethods(sess)
        fb.send_feedback(cls.fb1.json_for_send)
        fb.send_feedback(cls.fb2.json_for_send)
        fb.send_feedback(cls.fb3.json_for_send)
        fb.send_feedback(cls.fb4.json_for_send)
        fb.send_feedback(cls.fb5.json_for_send)
        fb.send_feedback(cls.fb6.json_for_send)
        requests.session().close()
        #cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        #cls.driver = webdriver.Chrome(DRIVER_PATH)
        #browser.set_driver(cls.driver)
        (LoginPage()
         .open()
         .login(cls.user1.email, cls.user1.password))

    @classmethod
    def tearDownClass(cls):
        browser.quit()
        #if cls.driver is not None:
        #    cls.driver.close()
        #    cls.driver.quit()

    def test_user_can_see_private_feedback_at_all_page(self):
        fb = FeedbackPage().open_all().get_feedback_by_text(self.fb1.text)
        assert fb is not None

    def test_user_can_see_private_feedback_at_to_you_page(self):
        fb = FeedbackPage().open_to_you().get_feedback_by_text(self.fb1.text)
        assert fb is not None

    def test_user_cant_see_private_feedback_at_added_to_praise_page(self):
        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(self.fb1.text)
        assert fb is None

    def test_user_can_see_public_feedback_at_added_to_praise_page(self):
        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(self.fb2.text)
        assert fb is not None

    def test_user_cant_see_private_feedback_to_another_user(self):
        fb = FeedbackPage().open_all().get_feedback_by_text(self.fb3.text)
        assert fb is None
        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(self.fb3.text)
        assert fb is None
        fb = FeedbackPage().open_to_you().get_feedback_by_text(self.fb3.text)
        assert fb is None

    def test_user_can_see_public_feedback_to_another_user(self):
        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(self.fb4.text)
        assert fb is not None

    def test_user_can_see_feedback_to_his_team(self):
        fb = FeedbackPage().open_all().get_feedback_by_text(self.fb5.text)
        assert fb is not None
        fb = FeedbackPage().open_to_you().get_feedback_by_text(self.fb5.text)
        assert fb is not None

    def test_user_cant_see_feedback_to_team_if_he_not_member(self):
        fb = FeedbackPage().open_all().get_feedback_by_text(self.fb6.text)
        assert fb is None
        fb = FeedbackPage().open_to_you().get_feedback_by_text(self.fb6.text)
        assert fb is None
        fb = FeedbackPage().open_added_to_praise().get_feedback_by_text(self.fb6.text)
        assert fb is None

    def setUp(self):
        assert True, True

    def tearDown(self):
        assert True, True


if __name__ == '__main__':
    unittest.main()
