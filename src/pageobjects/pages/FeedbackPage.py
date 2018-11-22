import time

from selene.api import *
from src.locators import *
from src.pages_url import *


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
                    return SurveyAnswerBlock(fb)
            return None

    def click_menu_all_link(self):
        self.menu_all_link.click()
        return FeedbackPage()

    def click_menu_to_you_link(self):
        self.menu_to_you_link.click()
        return FeedbackPage()

    def click_menu_added_to_praise_link(self):
        self.menu_added_to_praise_link.click()
        return FeedbackPage()

    def click_menu_via_surveys_link(self):
        self.menu_via_surveys_link.click()
        return FeedbackPage()

    def click_menu_via_reviews_link(self):
        self.menu_via_reviews_link.click()
        return FeedbackPage()

    def click_menu_sent_link(self):
        self.menu_sent_feedback_link.click()
        return FeedbackPage()

    def click_menu_flagged_link(self):
        self.menu_flagged_link.click()
        return FeedbackPage()

    def open_all(self):
        browser.open_url(FEEDBACK_ALL_URL)
        return FeedbackPage()

    def open_sent(self):
        browser.open_url(FEEDBACK_SENT_URL)
        return FeedbackPage()

    def open_to_you(self):
        browser.open_url(FEEDBACK_TO_YOU_URL)
        return FeedbackPage()

    def open_added_to_praise(self):
        browser.open_url(FEEDBACK_ADDED_TO_PRAISE_URL)
        return FeedbackPage()

    def open_via_surveys(self):
        browser.open_url(FEEDBACK_VIA_SURVEYS_URL)
        return FeedbackPage()

    def open_via_reviews(self):
        browser.open_url(FEEDBACK_VIA_REVIEWS_URL)
        return FeedbackPage()

    def open_flagged(self):
        browser.open_url(FEEDBACK_FLAGGED_URL)
        return FeedbackPage()


class FeedbackBlock(object):
    def __init__(self, fb):
        self.text = fb.element(by.xpath(FEEDBACK_BLOCK_FEEDBACK_TEXT)).text
        self.value = fb.element(by.xpath(FEEDBACK_BLOCK_VALUE_ICON))
        self.people = fb.element(FEEDBACK_BLOCK_PEOPLE_NAME)
        self.to_praise_link = fb.element(by.xpath(FEEDBACK_BLOCK_ADD_TO_PRAISE_LINK))
        self.flag_link = fb.element(by.xpath(FEEDBACK_BLOCK_FLAGGED_LINK))
        self.heart_icon = fb.element(by.xpath(FEEDBACK_BLOCK_LIKE_ICON))
        self.comment_icon = fb.element(by.xpath(FEEDBACK_BLOCK_COMMENT_ICON))
        self.more = fb.element(FEEDBACK_BLOCK_MORE_LINK)
        self.edit = fb.element(FEEDBACK_BLOCK_EDIT_LINK)
        self.delete = fb.element(FEEDBACK_BLOCK_DELETE_LINK)


class SurveyAnswerBlock(object):
    def __init__(self, fb):
        self.sender = fb.element(SURVEY_ANSWER_BLOCK_SENDER)
        self.question_text = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_QUESTION_TEXT))
        self.people = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_PEOPLE))
        self.answer_text = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_ANSWER_TEXT))
        self.add_to_praise_link = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_ADD_TO_PRAISE_LINK))
        self.flag_link = fb.element(by.xpath(SURVEY_ANSWER_BLOCK_FLAG_LINK))

