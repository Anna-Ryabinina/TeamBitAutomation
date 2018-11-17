import time

from selene.api import *
from src.locators import *
from pynput.keyboard import Controller, Key


class FeedbackRequestPopup(object):
    def __init__(self):
        self.popup = s(by.xpath(FEEDBACK_POPUP))
        self.recipient_input = s(FEEDBACK_POPUP_RECIPIENTS_TEXT_INPUT)
        self.text_input = s(by.xpath(FEEDBACK_POPUP_FEEDBACK_TEXT_INPUT))
        self.send_feedback_button = s(by.xpath(FEEDBACK_POPUP_SEND_FEEDBACK_BUTTON))
        self.add_value_icon = s(by.xpath(FEEDBACK_POPUP_ADD_VALUE_ICON))
        self.add_to_praise_icon = s(by.xpath(FEEDBACK_POPUP_MAKE_PUBLIC_ICON))
        self.fb_template_icon = s(by.xpath(FEEDBACK_POPUP_FEEDBACK_TEMPLATE_ICON))
        self.value_from_list = s(by.xpath(FEEDBACK_POPUP_VALUE_TO_CHOOSE))
        self.template_list = ss(by.xpath(FEEDBACK_POPUP_TEMPLATE_TO_CHOOSE))
        self.close_button = s(by.xpath(FEEDBACK_POPUP_CLOSE_ICON))
        self.recipient_name_list = s(by.xpath(FEEDBACK_POPUP_RECIPIENTS_NAME_LIST))
        self.value_added = s(FEEDBACK_POPUP_VALUE_PIC_ADDED)
        self.recipient_added = s(FEEDBACK_POPUP_RECIPIENT_ADDED)
        self.rq_template_icon = s(by.xpath(FEEDBACK_POPUP_REQUEST_TEMPLATE_ICON))
        self.send_request_button = s(by.xpath(FEEDBACK_POPUP_SEND_REQUEST_BUTTON))

    def type_recipient(self, name):
        keyboard = Controller()
        self.recipient_input.send_keys(name)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        return FeedbackRequestPopup()

    def add_value(self):
        self.add_value_icon.click()
        self.value_from_list.click()
        return FeedbackRequestPopup()

    def add_template_to_feedback(self):
        self.fb_template_icon.click()
        self.template_list[0].click()
        return FeedbackRequestPopup()

    def make_public(self):
        self.add_to_praise_icon.click()
        return FeedbackRequestPopup()

    def make_private(self):
        self.add_to_praise_icon.click()
        return FeedbackRequestPopup()

    def close(self):
        self.close_button.click()
        return FeedbackRequestPopup()

    def type_text(self, text):
        self.text_input.set(text)
        return FeedbackRequestPopup()

    def add_text(self, text):
        self.text_input.send_keys(text)
        return FeedbackRequestPopup()

    def add_template_to_request(self):
        self.rq_template_icon.click()
        self.template_list[0].click()
        return FeedbackRequestPopup()

    def click_send_feedback_button(self):
        self.send_feedback_button.click()
        return FeedbackRequestPopup()

    def click_send_request_button(self):
        self.send_request_button.click()
        return FeedbackRequestPopup()








