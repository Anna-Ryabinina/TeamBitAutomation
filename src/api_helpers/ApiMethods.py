from src.api_urls import *


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