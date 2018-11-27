from selene.api import *
from src.locators import *


class TeammateTableRow(object):

    def __init__(self, row):
        self.name_link = row.element(PEOPLE_TEAMMATE_NAME_LINK)
        self.send_feedback_button = row.element(by.xpath(PEOPLE_TEAMMATE_SEND_FEEDBACK_BUTTON))
        self.request_feedback_button = row.element(by.xpath(PEOPLE_TEAMMATE_REQUEST_FEEDBACK_BUTTON))
        self.make_admin_button = row.element(by.xpath(PEOPLE_TEAMMATE_MAKE_ADMIN_BUTTON))
        self.make_user_button = row.element(by.xpath(PEOPLE_TEAMMATE_MAKE_USER_BUTTON))
        self.delete_button = row.element(by.xpath(PEOPLE_TEAMMATE_DELETE_USER))
        self.row = row

    def make_admin(self):
        self.make_admin_button.click()
        return TeammateTableRow(self.row)

    def make_user(self):
        self.make_user_button.click()
        return TeammateTableRow(self.row)