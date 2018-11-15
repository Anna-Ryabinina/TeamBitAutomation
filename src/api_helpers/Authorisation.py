from src.api_urls import *


class Authorisation(object):

    def __init__(self, session):
        self.session = session

    def get_session(self):
        return self.session

    def login_with_email(self, user):
        payload = {
            "username": user.email,
            "password": user.password
        }
        r = self.session.post(LOGIN_API_URL, data=payload)
        return r