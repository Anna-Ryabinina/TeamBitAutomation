from selene.api import *
from src.locators import *
from src.pages_url import *
import time


class SurveyPage(object):

    def __init__(self):
        self.create_new_survey_button = s(by.xpath(SURVEY_CREATE_NEW_SURVEY_BUTTON))
        self.edit_button = s(by.xpath(SURVEY_INFO_EDIT_BUTTON))
        self.pause_button = s(by.xpath(SURVEY_INFO_PAUSE_BUTTON))
        self.back_button = s(by.xpath(SURVEY_INFO_BACK_BUTTON))

    def open(self):
        browser.open_url(SURVEY_PAGE_URL)
        time.sleep(0.5)
        return SurveyPage()

    def get_survey_by_text(self, text):
        srvs = ss(SURVEY_BLOCK)
        if len(srvs) == 0:
            return None
        else:
            for srv in srvs:
                if text in srv.element(SURVEY_BLOCK_TITLE).text:
                    return SurveyBlock(srv)
            return None


class SurveyBlock(object):
    def __init__(self, survey):
        self.title = survey.element(SURVEY_BLOCK_TITLE)
        self.paused_label = survey.element(SURVEY_BLOCK_PAUSED_STATUS)
        self.author = survey.element(SURVEY_BLOCK_AUTHOR)


