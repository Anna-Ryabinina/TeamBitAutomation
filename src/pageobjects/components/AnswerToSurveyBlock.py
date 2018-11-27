from selene.api import *
from src.locators import *


class AnswerToSurveyBlock(object):
    def __init__(self, fb):
        self.sender = fb.element(SURVEY_ANSWER_BLOCK_SENDER)
        self.question_text = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_QUESTION_TEXT))
        self.people = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_PEOPLE))
        self.answer_text = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_ANSWER_TEXT))
        self.add_to_praise_link = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_ADD_TO_PRAISE_LINK))
        self.flag_link = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_FLAG_LINK))
        self.fb = fb

    def add_to_praise(self):
        self.add_to_praise_link.click()
        return AnswerToSurveyBlock(self.fb)

    def remove_from_praise(self):
        self.add_to_praise_link.click()
        return AnswerToSurveyBlock(self.fb)

    def mark_with_flag(self):
        self.flag_link.click()
        return AnswerToSurveyBlock(self.fb)

    def unmark_with_flag(self):
        self.flag_link.click()
        return AnswerToSurveyBlock(self.fb)
