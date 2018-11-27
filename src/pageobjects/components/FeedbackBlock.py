from selene.api import *
from src.locators import *


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