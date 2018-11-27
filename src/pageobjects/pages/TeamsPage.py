from selene.api import *
from src.pages_url import *
from src.locators import *
import time


class TeamsPage(object):

    def __init__(self):
        self.create_new_team_button = s(by.xpath(TEAMS_CREATE_NEW_BUTTON))

    def open(self):
        browser.open_url(TEAMS_PAGE_URL)
        time.sleep(0.5)
        return TeamsPage()

    def get_team_row_by_id(self, id=0):
        teams = ss(TEAM_ROW)
        if len(teams) == 0:
            return None
        return TeamRow(teams[id])

    def get_team_row_by_name(self, team):
        teams = ss(TEAM_ROW)
        if len(teams) == 0:
            return None
        for t in teams:
            if team.name in t.element(by.xpath(TEAM_NAME)).text:
                return TeamRow(t)
        return None

    def leave_team_by_id(self, id=0):
        t = self.get_team_row_by_id(id)
        return t.leave_team()

    def join_team_by_id(self, id=0):
        t = self.get_team_row_by_id(id)
        return t.join_team()

    def leave_team(self, team):
        t = self.get_team_row_by_name(team)
        return t.leave_team()

    def join_team(self, team):
        t = self.get_team_row_by_name(team)
        return t.join_team()


class TeamRow(object):
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
        return TeamRow(self.row)

    def join_team(self):
        self.join_button.click()
        return TeamRow(self.row)