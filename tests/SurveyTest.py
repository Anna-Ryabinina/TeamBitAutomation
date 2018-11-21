import unittest
import time
from selene.api import *
from tests.BaseTest import BaseTest
from src.pageobjects.pages.SurveyPage import SurveyPage
from src.pageobjects.popups.SurveyPopup import SurveyPopup
from src.pageobjects.pages.LogInPage import LoginPage
from src.pageobjects.pages.RequestPage import RequestsPage
from src.test_data_generators.User import User
from src.test_data import *
from src.api_helpers.ApiMethods import ApiMethods
from src.test_data_generators.SurveyPayload import SurveyPayload
import requests


class SurveyTest(BaseTest):

    def test_user_can_create_text_survey(self):
        user1 = User(user_1)
        title = 'test_user_can_create_survey ' + self.execute_date
        question_text = 'text_public' + self.execute_date
        LoginPage().open().login_as_user(user1)
        time.sleep(0.5)
        SurveyPage().open().create_new_survey_button.click()
        SurveyPopup().create_empty().type_name(title).get_question_by_id().type_question(question_text)
        SurveyPopup().run_now()
        time.sleep(0.5)
        survey = SurveyPage().get_survey_by_text(title)
        assert survey is not None
        sess = requests.session()
        ApiMethods(sess).login_as_user(user1)
        survey = ApiMethods(sess).get_survey_by_title(title)
        assert survey is not None


    def test_api(self):
        user1 = User(user_1)
        user2 = User(user_2)
        user3 = User(user_3)
        user4 = User(user_4)
        name = 'test ' + self.execute_date
        print('Title: ' + name)
        sess = requests.session()
        ApiMethods(sess).login_as_user(user1)
        payload = SurveyPayload()
        request_data = (payload
                        .set_title(name)
                        .add_text_question('1 text public question')
                        .add_text_question('2 text anonymous question', is_anonymous=True)
                        .add_rating_question('3 rating public question')
                        .add_rating_question('4 rating anonymous question', is_anonymous=True)
                        .set_receivers([user1, user2, user3])
                        .set_viewers([user1, user2, user4])
                        .generate_new_survey_data_run_now())
        print(payload.title)
        print(payload.questions)
        print(payload.viewers)
        print(payload.receivers)
        print(request_data)
        r = ApiMethods(sess).create_survey(request_data)
        print(r.status_code)
        sess.close()


if __name__ == '__main__':
    unittest.main()
