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

    def test_something(self):
        user1 = User(user_1)
        title = 'test ' + self.execute_date
        question = 'test q ' + self.execute_date
        LoginPage().open().login(user1.email, user1.password)
        time.sleep(0.5)
        SurveyPage().open().create_new_survey_button.click()
        SurveyPopup().popup.should(be.visible)
        SurveyPopup().create_empty().type_name(title)
        q = SurveyPopup().get_question_by_id()
        q.type_question(question).choose_rating_option().choose_anonymous_option()
        SurveyPopup().run_now()
        browser.driver().refresh()
        survey = SurveyPage().get_survey_by_text(title)
        assert survey is not None
        RequestsPage().open()
        r = RequestsPage().get_request_by_text(question)
        assert r is not None

    def test_api(self):
        user1 = User(user_1)
        user2 = User(user_2)
        user3 = User(user_3)
        user4 = User(user_4)
        name = 'test ' + self.execute_date
        print('Title: ' + name)
        sess = requests.session()
        ApiMethods(sess).login_as_user(user1)
        request_data = (SurveyPayload()
                        .set_title(name)
                        .add_text_question('1 text public question')
                        .add_text_question('2 text anonymous question', is_anonymous=True)
                        .add_rating_question('3 rating public question')
                        .add_rating_question('4 rating anonymous question', is_anonymous=True)
                        .set_receivers([user1, user2, user3])
                        .set_viewers([user1, user2, user4])
                        .generate_new_survey_data_run_now())
        print(request_data)
        r = ApiMethods(sess).create_survey(request_data)
        print(r.status_code)
        sess.close()


if __name__ == '__main__':
    unittest.main()
