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
from src.pageobjects.popups.FeedbackRequestPopup import FeedbackRequestPopup
from src.pageobjects.pages.FeedbackPage import FeedbackPage
from src.pageobjects.pages.SurveyDetailsPage import SurveyDetailsPage


class SurveyTest(BaseTest):

    def test_user_can_create_and_answer_survey_with_all_question_types(self):
        user1 = User(user_1)
        title = 'test_types ' + self.execute_date
        question_text_public = 'text_public ' + self.execute_date
        question_text_anonym = 'text_anonym ' + self.execute_date
        question_rating_public = 'rating_public ' + self.execute_date
        question_rating_anonym = 'rating_anonym ' + self.execute_date
        LoginPage().open().login_as_user(user1)
        time.sleep(0.1)
        SurveyPage().open().create_new_survey_button.click()

        (SurveyPopup()
         .create_empty()
         .type_name(title)
         .add_question()
         .add_question()
         .add_question()
         .get_question_by_id()
         .type_question(question_text_public))

        (SurveyPopup()
         .get_question_by_id(1)
         .type_question(question_text_anonym)
         .choose_anonymous_option())

        (SurveyPopup()
         .get_question_by_id(2)
         .type_question(question_rating_public)
         .choose_rating_option())

        (SurveyPopup()
         .get_question_by_id(3)
         .type_question(question_rating_anonym)
         .choose_rating_option()
         .choose_anonymous_option())

        SurveyPopup().run_now()
        time.sleep(0.5)

        survey = SurveyPage().get_survey_by_text(title)
        assert survey is not None
        sess = requests.session()
        ApiMethods(sess).login_as_user(user1)
        survey = ApiMethods(sess).get_survey_by_title(title)
        assert survey is not None
        assert len(survey.questions)==4
        assert survey.questions[0]['type']==2
        assert survey.questions[0]['is_anonymous'] is None
        assert survey.questions[1]['type']==2
        assert survey.questions[1]['is_anonymous'] is True
        assert survey.questions[2]['type']==1
        assert survey.questions[2]['is_anonymous'] is None
        assert survey.questions[3]['type']==1
        assert survey.questions[3]['is_anonymous'] is True

        request = RequestsPage().open().get_request_by_text(question_text_public)
        assert request is not None

        request.send_feedback_button.click()

        FeedbackRequestPopup().popup.should(be.visible)

        FeedbackRequestPopup().type_text('answer text public')
        time.sleep(0.2)
        FeedbackRequestPopup().click_send_feedback_button()
        time.sleep(0.2)
        FeedbackRequestPopup().type_text('answer text anonym')
        time.sleep(0.2)
        FeedbackRequestPopup().click_send_feedback_button()
        time.sleep(0.2)
        FeedbackRequestPopup().click_rating_item(0)
        time.sleep(1)
        FeedbackRequestPopup().click_rating_item(1)
        time.sleep(0.2)
        FeedbackRequestPopup().popup.should_not(be.visible)

        FeedbackPage().open_sent()
        time.sleep(0.5)
        f = FeedbackPage().get_survey_answer_by_text(question_text_public)
        assert f is not None
        f = FeedbackPage().get_survey_answer_by_text(question_text_anonym)
        assert f is not None
        f = FeedbackPage().get_survey_answer_by_text(question_rating_public)
        assert f is not None
        f = FeedbackPage().get_survey_answer_by_text(question_rating_anonym)
        assert f is not None

    def test_user_can_pause_survey(self):
        user = User(user_1)
        title = 'test_deactivate ' + self.execute_date
        payload = SurveyPayload(title)
        survey = payload.add_text_question('question_1').add_text_question('question_2').generate_new_survey_data_run_now()
        sess = requests.session()
        ApiMethods(sess).login_as_user(user)
        response = ApiMethods(sess).create_survey(survey)
        print(response.json()['id'])

        LoginPage().open().login_as_user(user)
        time.sleep(0.5)

        SurveyDetailsPage().open_by_id(response.json()['id'])
        time.sleep(0.5)

        SurveyDetailsPage().pause_survey()
        SurveyDetailsPage().pause_button.should(have.text('live'))

        survey = ApiMethods(sess).get_survey_by_id(response.json()['id'])
        assert survey.is_active is True

        SurveyPage().open().get_survey_by_text(title).paused_label.should(be.visible)

    def test_user_can_deactivate_survey(self):
        user = User(user_1)
        title = 'test_activate ' + self.execute_date
        payload = SurveyPayload(title)
        survey = payload.add_text_question('question_1').add_text_question(
            'question_2').generate_new_survey_data_run_now()
        sess = requests.session()
        ApiMethods(sess).login_as_user(user)
        id = ApiMethods(sess).create_survey(survey).json()['id']
        ApiMethods(sess).deactivate_survey(id)

        LoginPage().open().login_as_user(user)
        time.sleep(0.5)

        SurveyDetailsPage().open_by_id(id)
        time.sleep(0.5)

        SurveyDetailsPage().set_survey_live()
        SurveyDetailsPage().pause_button.should(have.text('Pause'))

        survey = ApiMethods(sess).get_survey_by_id(id)
        assert survey.is_active is False

        SurveyPage().open().get_survey_by_text(title).paused_label.should_not(be.visible)


if __name__ == '__main__':
    unittest.main()
