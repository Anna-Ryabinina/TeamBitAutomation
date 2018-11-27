from selene.api import *
from src.locators import *
from src.pageobjects.components.TeammateTableRow import TeammateTableRow
from src.pages_url import *
import time


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
        return TeammateTableRow(people[id])

    def get_teammate_row_by_user(self, user):
        people = ss(PEOPLE_TEAMMATE_ROW)
        if len(people) == 0:
            return None
        for man in people:
            if user.full_name in man.element(PEOPLE_TEAMMATE_NAME_LINK).text:
                return TeammateTableRow(man)
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




