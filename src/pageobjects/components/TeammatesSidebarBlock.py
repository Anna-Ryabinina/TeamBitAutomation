from selene.api import *
from src.locators import *
from src.pageobjects.components.FeedbackRequestPopup import FeedbackRequestPopup


class TeammatesSidebarBlock(object):
    def __init__(self):
        self.invite_link = s(SIDEBAR_INVITE_LINK)
        self.teammates = ss(SIDEBAR_TEAMMATE)

    def get_teammate_by_id(self, id):
        return self.teammates[id]

    def get_teammate_by_name(self, user):
        for t in self.teammates:
            if user.first_name in t.element(by.xpath(SIDEBAR_TEAMMATE_NAME)).text:
                return t
        return None

    def send_feedback_to_user(self, user):
        t = self.get_teammate_by_name(user)
        t.element(SIDEBAR_TEAMMATE_FEEDBACK_BUTTON).click()
        return FeedbackRequestPopup()

    def request_feedback_from_user(self, user):
        t = self.get_teammate_by_name(user)
        t.element(SIDEBAR_TEAMMATE_REQUEST_BUTTON).click()
        return FeedbackRequestPopup()

    def send_feedback_by_id(self, id=0):
        self.get_teammate_by_id(id).element(SIDEBAR_TEAMMATE_FEEDBACK_BUTTON).click()
        return FeedbackRequestPopup()

    def request_feedback_by_id(self, id=0):
        self.get_teammate_by_id(id).element(SIDEBAR_TEAMMATE_REQUEST_BUTTON).click()
        return FeedbackRequestPopup()