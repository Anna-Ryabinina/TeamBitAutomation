from selene.api import *
from src.locators import *
from src.pages_url import *
import time


class SurveyDetailsPage(object):

    def __init__(self):
        self.back_button = s(by.xpath(SURVEY_INFO_BACK_BUTTON))
        self.edit_button = s(by.xpath(SURVEY_INFO_EDIT_BUTTON))
        self.pause_button = s(by.xpath(SURVEY_INFO_PAUSE_BUTTON))
        self.filter_list = s(by.xpath(SURVEY_INFO_FILTER))

    def open_by_id(self, id):
        browser.open_url(SURVEY_DETAILS_URL + str(id))
        time.sleep(0.5)
        return SurveyDetailsPage()

    def click_back(self):
        self.back_button.click()
        return SurveyDetailsPage()

    def pause_survey(self):
        self.pause_button.click()
        return SurveyDetailsPage()

    def set_survey_live(self):
        self.pause_button.click()
        return SurveyDetailsPage()