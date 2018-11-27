from selene.api import *
from src.locators import *


class SurveyBlock(object):
    def __init__(self, survey):
        self.title = survey.element(SURVEY_BLOCK_TITLE)
        self.paused_label = survey.element(SURVEY_BLOCK_PAUSED_STATUS)
        self.author = survey.element(SURVEY_BLOCK_AUTHOR)