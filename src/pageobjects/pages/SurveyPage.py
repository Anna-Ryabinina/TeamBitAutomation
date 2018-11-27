from selene.api import *
from src.locators import *
from src.pageobjects.components.SurveyBlock import SurveyBlock
from src.pages_url import *
import time
from src.pageobjects.components.SurveyPopup import SurveyPopup


class SurveyPage(object):

    def __init__(self):
        self.create_new_survey_button = s(by.xpath(SURVEY_CREATE_NEW_SURVEY_BUTTON))

    def open(self):
        browser.open_url(SURVEY_PAGE_URL)
        time.sleep(0.5)
        return self

    def get_survey_by_text(self, text):
        srvs = ss(SURVEY_BLOCK)
        if len(srvs) == 0:
            return None
        else:
            for srv in srvs:
                if text in srv.element(SURVEY_BLOCK_TITLE).text:
                    return SurveyBlock(srv)
            return None

    def click_create_new_survey(self):
        self.create_new_survey_button()
        return SurveyPopup()





