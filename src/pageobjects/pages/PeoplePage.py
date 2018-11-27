from selene.api import *
from src.locators import *
from src.pages_url import *


class PeoplePage(object):

    def __init__(self):
        self.invite_button = s(by.xpath(PEOPLE_INVITE_BUTTON))

    def open(self):
        browser.open_url(PEOPLE_PAGE_URL)
        time.sleep(0.5)
        return PeoplePage()

    def click_invite_button(self):
        self.invite_button.click()
        return PeoplePage()

    def get_teammate_row_by_id(self, id=0):
        people = ss(PEOPLE_TEAMMATE_ROW)
        if len(people) == 0:
            return None
        return TeammateRow(people[id])

    def get_teammate_row_by_user(self, user):
        people = ss(PEOPLE_TEAMMATE_ROW)
        if len(people) == 0:
            return None
        for man in people:
            if user.full_name in man.element(PEOPLE_TEAMMATE_NAME_LINK).text:
                return TeammateRow(man)
        return None

    def make_admin_by_id(self, id=0):
        teammate = self.get_teammate_row_by_id(id)
        return teammate.make_admin()

    def make_user_by_id(self, id=0):
        teammate = self.get_teammate_row_by_id(id)
        return teammate.make_user()

    def make_user(self, user):
        teammate = self.get_teammate_row_by_user(user)
        return teammate.make_user()

    def make_admin(self, user):
        teammate = self.get_teammate_row_by_user(user)
        return teammate.make_admin()


class TeammateRow(object):

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
        return TeammateRow(self.row)

    def make_user(self):
        self.make_user_button.click()
        return TeammateRow(self.row)