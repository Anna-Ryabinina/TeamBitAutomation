from selene.api import *
from src.locators import *
from src.pageobjects.components.RequestBlock import RequestBlock
from src.pageobjects.components.FeedbackRequestPopup import FeedbackRequestPopup
from src.pages_url import *
import time


class RequestsPage(object):
    def __init__(self):
        self.menu_pending_link = s(by.xpath(REQUEST_MENU_PENDING_REQUESTS))
        self.menu_sent_link = s(by.xpath(REQUEST_MENU_SENT_REQUESTS))
        self.menu_resolved_link = s(by.xpath(REQUEST_MENU_RESOLVED_REQUESTS))
        self.request_feedback_button = s(by.xpath(REQUEST_REQUESTS_FEEDBACK_BUTTON))

    def get_request_by_text(self, text):
        rqs = ss(REQUEST_BLOCK)
        if len(rqs) == 0:
            return None
        else:
            for rq in rqs:
                if text in rq.element(by.xpath(REQUEST_BLOCK_TEXT)).text:
                    return RequestBlock(rq)
            return None

    def click_menu_pending_link(self):
        self.menu_pending_link.click()
        return self

    def click_menu_sent_link(self):
        self.menu_sent_link.click()
        return self

    def click_menu_resolved_link(self):
        self.menu_resolved_link.click()
        return self

    def open(self):
        browser.open_url(REQUEST_PAGE_URL)
        time.sleep(0.5)
        return self

    def open_sent(self):
        browser.open_url(REQUEST_SENT_URL)
        time.sleep(0.5)
        return self

    def open_resolved(self):
        browser.open_url(REQUEST_RESOLVED_URL)
        time.sleep(0.5)
        return self

    def click_request_feedback(self):
        self.request_feedback_button.click()
        return FeedbackRequestPopup()


