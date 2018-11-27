import time

from selene.api import *
from src.locators import *
from src.pageobjects.components.AnswerToSurveyBlock import AnswerToSurveyBlock
from src.pageobjects.components.FeedbackBlock import FeedbackBlock
from src.pages_url import *
from src.pageobjects.components.FeedbackRequestPopup import FeedbackRequestPopup


class FeedbackPage(object):
    def __init__(self):
        self.logo = s(FEEDBACK_LOGO)
        self.send_feedback_button = s(by.xpath(FEEDBACK_SEND_FEEDBACK_BUTTON))
        self.menu_all_link = s(by.xpath(FEEDBACK_MENU_ALL_LINK))
        self.menu_to_you_link = s(by.xpath(FEEDBACK_MENU_TO_YOU_LINK))
        self.menu_added_to_praise_link = s(by.xpath(FEEDBACK_MENU_ADDED_TO_PRAISE))
        self.menu_via_surveys_link = s(by.xpath(FEEDBACK_MENU_VIA_SURVEYS_LINK))
        self.menu_via_reviews_link = s(by.xpath(FEEDBACK_MENU_VIA_REVIEWS_LINK))
        self.menu_sent_feedback_link = s(by.xpath(FEEDBACK_MENU_SENT_LINK))
        self.menu_flagged_link = s(by.xpath(FEEDBACK_MENU_FLAGGED))

    def get_feedback_by_text(self, text):
        fbs = ss(FEEDBACK_BLOCK)
        if len(fbs) == 0:
            return None
        else:
            for fb in fbs:
                if text in fb.element(by.xpath(FEEDBACK_BLOCK_FEEDBACK_TEXT)).text:
                    return FeedbackBlock(fb)
            return None

    def get_survey_answer_by_text(self, text):
        fbs = ss(SURVEY_ANSWER_BLOCK)
        if len(fbs) == 0:
            return None
        else:
            for fb in fbs:
                if text in fb.element(by.xpath(SURVEY_ANSWER_BLOCK_QUESTION_TEXT)).text:
                    return AnswerToSurveyBlock(fb)
            return None

    def click_send_feedback(self):
        self.send_feedback_button.click()
        return FeedbackRequestPopup()

    def click_menu_all_link(self):
        self.menu_all_link.click()
        return self

    def click_menu_to_you_link(self):
        self.menu_to_you_link.click()
        return self

    def click_menu_added_to_praise_link(self):
        self.menu_added_to_praise_link.click()
        return self

    def click_menu_via_surveys_link(self):
        self.menu_via_surveys_link.click()
        return self

    def click_menu_via_reviews_link(self):
        self.menu_via_reviews_link.click()
        return self

    def click_menu_sent_link(self):
        self.menu_sent_feedback_link.click()
        return self

    def click_menu_flagged_link(self):
        self.menu_flagged_link.click()
        return self

    def open_all(self):
        browser.open_url(FEEDBACK_ALL_URL)
        time.sleep(0.5)
        return self

    def open_sent(self):
        browser.open_url(FEEDBACK_SENT_URL)
        time.sleep(0.5)
        return self

    def open_to_you(self):
        browser.open_url(FEEDBACK_TO_YOU_URL)
        time.sleep(0.5)
        return self

    def open_added_to_praise(self):
        browser.open_url(FEEDBACK_ADDED_TO_PRAISE_URL)
        time.sleep(0.5)
        return self

    def open_via_surveys(self):
        browser.open_url(FEEDBACK_VIA_SURVEYS_URL)
        time.sleep(0.5)
        return self

    def open_via_reviews(self):
        browser.open_url(FEEDBACK_VIA_REVIEWS_URL)
        time.sleep(0.5)
        return self

    def open_flagged(self):
        browser.open_url(FEEDBACK_FLAGGED_URL)
        time.sleep(0.5)
        return self






