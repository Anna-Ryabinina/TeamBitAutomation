from selene.api import *

from src.pageobjects.pages.FeedbackPage import FeedbackBlock
from src.pages_url import *
from src.locators import *
import time


class TeammatePage(object):

    def __init__(self):
        self.edit_button = s(by.xpath(TEAMMATE_EDIT_BUTTON))
        self.send_feedback_button = s(by.xpath(TEAMMATE_SEND_FEEDBACK_BUTTON))
        self.request_feedback_button = s(by.xpath(TEAMMATE_REQUEST_FEEDBACK_BUTTON))

    def get_feedback_by_text(self, text):
        fbs = ss(FEEDBACK_BLOCK)
        if len(fbs) == 0:
            return None
        else:
            for fb in fbs:
                if text in fb.element(by.xpath(FEEDBACK_BLOCK_FEEDBACK_TEXT)).text:
                    return FeedbackBlock(fb)
            return None

    def click_edit_button(self):
        self.edit_button.click()

    def click_send_feedback_button(self):
        self.send_feedback_button.click()

    def click_request_feedback_button(self):
        self.request_feedback_button.click()

    def open_by_user_id(self, id):
        browser.open_url(TEAMMATE_PAGE_URL + str(id))
        time.sleep(0.5)
        return TeammatePage()


