from selene.api import *
from src.locators import *
from pynput.keyboard import Controller, Key


class SurveyPopup(object):
    def __init__(self):
        self.popup = s(by.css(SURVEY_POPUP))
        self.close_button = s(by.xpath(SURVEY_POPUP_CLOSE_BUTTON))
        self.empty_template = s(by.xpath(SURVEY_POPUP_CREATE_EMPTY_SURVEY_BUTTON))
        self.choose_another_template_link = s(by.xpath(SURVEY_POPUP_OR_CHOOSE_ANOTHER_TEMPLAY_LINK))
        self.title_input = s(by.xpath(SURVEY_POPUP_SURVEY_NAME_TEXT_INPUT))
        self.choose_date_time_button = s(SURVEY_POPUP_CHOOSE_DATE_TIME_BUTTON)
        self.run_now_button = s(by.xpath(SURVEY_POPUP_RUN_NOW_BUTTON))
        self.who_request_from_input = s(by.xpath(SURVEY_POPUP_WHO_REQUEST_FROM_INPUT))
        self.who_able_to_see_input = s(by.xpath(SURVEY_POPUP_WHO_ABLE_TO_SEE_INPUT))
        self.add_question_button = s(by.xpath(SURVEY_POPUP_ADD_QUESTION_BUTTON))
        self.questions = ss(by.xpath(SURVEY_POPUP_QUESTION_SECTION))

    def close(self):
        self.close_button.click()
        return SurveyPopup()

    def create_empty(self):
        self.empty_template.click()
        return SurveyPopup()

    def choose_another_template(self):
        self.choose_another_template_link.click()
        return SurveyPopup()

    def add_question(self):
        self.add_question_button.click()
        return SurveyPopup()

    def choose_date_time(self):
        self.choose_date_time_button.click()
        return SurveyPopup()

    def run_now(self):
        self.run_now_button.click()
        return SurveyPopup()

    def type_who_request_feedback_from(self, name):
        keyboard = Controller()
        self.who_request_from_input.send_keys(name)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        return SurveyPopup()

    def type_who_able_to_see(self, name):
        keyboard = Controller()
        self.who_able_to_see_input.send_keys(name)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        return SurveyPopup()


class SurveyQuestionBlock(object):
    def __init__(self, question):
        self.question_input = question.element(SURVEY_POPUP_QUESTION_TEXT_INPUT)
        self.remove_question_button = question.element(SURVEY_POPUP_REMOVE_QUESTION_BUTTON)
        self.text_option = question.element(SURVEY_POPUP_QUESTION_TEXT_OPTION_BUTTON)
        self.rating_option = question.element(SURVEY_POPUP_QUESTION_RATING_OPTION_BUTTON)
        self.public_option = question.element(SURVEY_POPUP_QUESTION_PUBLIC_OPTION_BUTTON)
        self.anonymous_option = question.element(SURVEY_POPUP_QUESTION_ANONYMOUS_OPTION_BUTTON)
