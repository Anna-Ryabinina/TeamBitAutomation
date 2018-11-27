from selene.api import *
from src.locators import *


class SurveyQuestionBlock(object):
    def __init__(self, question):
        self.question_input = question.element(by.xpath(SURVEY_POPUP_QUESTION_TEXT_INPUT))
        self.remove_question_button = question.element(by.xpath(SURVEY_POPUP_REMOVE_QUESTION_BUTTON))
        self.text_option = question.element(by.xpath(SURVEY_POPUP_QUESTION_TEXT_OPTION_BUTTON))
        self.rating_option = question.element(by.xpath(SURVEY_POPUP_QUESTION_RATING_OPTION_BUTTON))
        self.public_option = question.element(by.xpath(SURVEY_POPUP_QUESTION_PUBLIC_OPTION_BUTTON))
        self.anonymous_option = question.element(by.xpath(SURVEY_POPUP_QUESTION_ANONYMOUS_OPTION_BUTTON))
        self.question = question

    def type_question(self, text):
        self.question_input.set(text)
        return self

    def choose_text_option(self):
        self.text_option.click()
        return self

    def choose_rating_option(self):
        self.rating_option.click()
        return self

    def choose_public_option(self):
        self.public_option.click()
        return self

    def choose_anonymous_option(self):
        self.anonymous_option.click()
        return self

    def delete_question(self):
        self.remove_question_button.click()
        return self
