from selene.api import *
from src.locators import *


class RequestBlock(object):
    def __init__(self, rq):
        self.text = rq.element(by.xpath(REQUEST_BLOCK_TEXT)).text
        self.send_feedback_button = rq.element(by.xpath(REQUEST_BLOCK_SEND_FEEDBACK_BUTTON))
        self.dismiss_link = rq.element(by.xpath(REQUEST_BLOCK_DISMISS_LINK))