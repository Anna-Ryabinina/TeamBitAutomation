import datetime
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.pageobjects.pages.TeammatePage import TeammatePage
from src.pageobjects.pages.FeedbackPage import FeedbackPage
from src.pageobjects.pages.TeamsPage import TeamsPage
from src.pageobjects.popups.FeedbackRequestPopup import FeedbackRequestPopup
from src.pageobjects.pages.LogInPage import LoginPage
from src.test_data_generators.User import User
from tests.BaseTest import BaseTest
from selene.api import *
from src.test_data import *
from src.pageobjects.blocks.TeammatesSidebarBlock import TeammatesSidebarBlock
from src.pageobjects.pages.RequestPage import RequestsPage
from src.pageobjects.pages.PeoplePage import PeoplePage
import time

class FeedbackFormElementsTests(BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.execute_date = datetime.datetime.today().strftime('%c')
        #cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(DRIVER_PATH)
        #browser.set_driver(cls.driver)
        user1 = User(user_1)
        LoginPage().open().login(user1.email, user1.password)
        time.sleep(0.5)

    def setUp(self):
        assert True

    def tearDown(self):
        assert True

    @classmethod
    def tearDownClass(cls):
        browser.quit()
        #if cls.driver is not None:
        #    cls.driver.close()
        #    cls.driver.quit()

    def test_feedback_form_opens_from_feedback_page(self):

        user2 = User(user_2)


        (FeedbackPage()
         .send_feedback_button.click())

        (FeedbackRequestPopup()
         .popup.should(be.visible))

        (FeedbackRequestPopup()
         .send_feedback_button.should_not(be.enabled))

        (FeedbackRequestPopup()
         .add_value()
         .value_added.should(be.visible))

        (FeedbackRequestPopup()
         .add_template_to_feedback()
         .text_input.should_not(be.empty))

        (FeedbackRequestPopup()
         .type_recipient(user2.full_name)
         .recipient_added.should(be.visible))

        (FeedbackRequestPopup()
         .make_public()
         .send_feedback_button.should(have.text('public')))

        (FeedbackRequestPopup()
         .make_private()
         .send_feedback_button.should(have.text('private')))

        (FeedbackRequestPopup()
         .text_input.send_keys('test'))

        (FeedbackRequestPopup()
         .send_feedback_button.should(be.enabled))

        (FeedbackRequestPopup()
         .close()
         .popup.should_not(be.visible))


    def test_feedback_form_opens_from_sidebar(self):
        TeammatesSidebarBlock().send_feedback_by_id()
        FeedbackRequestPopup().popup.should(be.visible)

    def test_feedback_form_opens_from_teammate_page(self):
        TeammatePage().open_by_user_id(User(user_2).id)
        TeammatePage().click_send_feedback_button()
        FeedbackRequestPopup().popup.should(be.visible)

    def test_feedback_form_opens_from_team_page(self):
        TeamsPage().open().get_team_row_by_id().send_feedback_button.click()
        FeedbackRequestPopup().popup.should(be.visible)

    def test_request_form_opens_from_request_page(self):
        RequestsPage().open().request_feedback_button.click()
        FeedbackRequestPopup().popup.should(be.visible)

    def test_request_form_opens_from_sidebar(self):
        FeedbackPage().open_all()
        TeammatesSidebarBlock().request_feedback_by_id()
        FeedbackRequestPopup().popup.should(be.visible)

    def test_request_form_opens_from_teammate_page(self):
        TeammatePage().open_by_user_id(User(user_2).id).click_request_feedback_button()
        FeedbackRequestPopup().popup.should(be.visible)

    def test_request_form_openst_from_team_page(self):
        TeamsPage().open().get_team_row_by_id().send_feedback_button.click()
        FeedbackRequestPopup().popup.should(be.visible)

    def test_feedback_form_opens_from_people_page(self):
        PeoplePage().open().get_teammate_row_by_id().send_feedback_button.click()
        FeedbackRequestPopup().popup.should(be.visible)

    def test_request_form_opens_from_people_page(self):
        PeoplePage().open().get_teammate_row_by_id().request_feedback_button.click()
        FeedbackRequestPopup().popup.should(be.visible)


if __name__ == '__main__':
    unittest.main()
