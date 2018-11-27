from src.api_urls import *
from src.test_data_generators.SurveyPayload import SurveyPayload
from src.test_data_generators.FeedbackPayload import FeedbackPayload


class ApiMethods(object):

    def __init__(self, session):
        self.session = session

    def send_feedback(self, payload):
        r = self.session.post(SEND_FEEDBACK_API_URL, json=payload)
        return r

    def send_request(self, payload):
        r = self.session.post(SEND_REQUEST_API_URL, json=payload)
        return r

    def create_survey(self, payload):
        r = self.session.post(CREATE_SURVEY_URL, json=payload)
        return r

    def login_as_user(self, user):
        payload = {
            "username": user.email,
            "password": user.password
        }
        r = self.session.post(LOGIN_API_URL, data=payload)
        return r

    def get_surveys_on_page(self):
        r = self.session.get(GET_SURVEYS_URL)
        return r

    def get_survey_by_title(self, title):
        surveys = self.get_surveys_on_page().json()
        for survey in surveys:
            if title in survey['name']:
                s = SurveyPayload().generate_from_json(survey)
                return s
        return None

    def get_all_feedback(self):
        r = self.session.get(GET_ALL_FEEDBACK_URL)
        return r

    def get_feedback_by_text(self, text):
        feedbacks = self.get_all_feedback().json()
        for feedback in feedbacks:
            if text in feedback['text']:
                s = FeedbackPayload().generate_feedback_from_json(feedback)
                return s
        return None

    def get_survey_by_id(self, id):
        r = self.session.get(GET_SURVEYS_URL + str(id))
        return SurveyPayload().generate_from_json(r.json())


    def deactivate_survey(self, id):
        return self.session.put(GET_SURVEYS_URL + str(id) + '/deactivate')

    def activate_survey(self, id):
        return self.session.put(GET_SURVEYS_URL + str(id) + '/activate')

