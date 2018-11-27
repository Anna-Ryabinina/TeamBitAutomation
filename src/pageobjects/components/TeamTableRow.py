from selene.api import *
from src.locators import *


class TeamTableRow(object):
    def __init__(self, row):
        self.row = row
        self.name = row.element(by.xpath(TEAM_NAME))
        self.send_feedback_button = row.element(by.xpath(TEAM_SEND_FEEDBACK_BUTTON))
        self.request_feedback_button = row.element(by.xpath(TEAM_REQUEST_FEEDBACK_BUTTON))
        self.edit_button = row.element(by.xpath(TEAM_EDIT_BUTTON))
        self.leave_button = row.element(by.xpath(TEAM_LEAVE_BUTTON))
        self.join_button = row.element(by.xpath(TEAM_JOIN_BUTTON))

    def leave_team(self):
        self.leave_button.click()
        return TeamTableRow(self.row)

    def join_team(self):
        self.join_button.click()
        return TeamTableRow(self.row)