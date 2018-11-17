from selene.api import *
from src.locators import *
from src.pages_url import *


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
        return RequestsPage()

    def click_menu_sent_link(self):
        self.menu_sent_link.click()
        return RequestsPage()

    def click_menu_resolved_link(self):
        self.menu_resolved_link.click()
        return RequestsPage()

    def open(self):
        browser.open_url(REQUEST_PAGE_URL)
        return RequestsPage()

    def open_sent(self):
        browser.open_url(REQUEST_SENT_URL)
        return RequestsPage()

    def open_resolved(self):
        browser.open_url(REQUEST_RESOLVED_URL)
        return RequestsPage()


class RequestBlock(object):
    def __init__(self, rq):
        self.text = rq.element(by.xpath(REQUEST_BLOCK_TEXT)).text
        self.send_feedback_button = rq.element(by.xpath(REQUEST_BLOCK_SEND_FEEDBACK_BUTTON))
        self.dismiss_link = rq.element(by.xpath(REQUEST_BLOCK_DISMISS_LINK))