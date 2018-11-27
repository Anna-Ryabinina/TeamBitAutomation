from selene.api import *
from src.locators import *
from src.pageobjects.pages.FeedbackPage import FeedbackPage
from src.pageobjects.pages.SurveyPage import SurveyPage
from src.pageobjects.pages.RequestPage import RequestsPage


class MainMenuBlock(object):
    def __init__(self):
        self.feedback = s(MAIN_MENU_FEEDBACK)
        self.requests = s(MAIN_MENU_REQUESTS)
        self.surveys = s(MAIN_MENU_SURVEYS)
        self.reviews = s(MAIN_MENU_REVIEWS)

    def click_feedback(self):
        self.feedback.click()
        return FeedbackPage()

    def click_requests(self):
        self.requests.click()
        return RequestsPage()

    def click_surveys(self):
        self.surveys.click()
        return SurveyPage()
