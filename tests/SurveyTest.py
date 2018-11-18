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
        r.


if __name__ == '__main__':
    unittest.main()
