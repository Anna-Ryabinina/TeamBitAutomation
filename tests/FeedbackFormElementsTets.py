import datetime
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.pages.pages.FeedbackPage import FeedbackPage
from src.pages.popups.FeedbackRequestPopup import FeedbackRequestPopup
from src.pages.pages.LogInPage import LoginPage
from src.test_data_generators.User import User
from tests.BaseTest import BaseTest
from selene.api import *
from src.test_data import *

class FeedbackFormElementsTests(BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.execute_date = datetime.datetime.today().strftime('%c')
        print('Test started: ' + cls.execute_date)
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(DRIVER_PATH)
        browser.set_driver(cls.driver)
        user1 = User(user_1)
        LoginPage().open().login(user1.email, user1.password)

    def setUp(self):
        assert True

    def tearDown(self):
        assert True

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.close()
            cls.driver.quit()

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


    def test_feedback_form_openes_from_sidebar(self):
        assert True

    def test_feedback_form_opens_from_teammate_page(self):
        assert True

    def test_feedback_form_opens_from_team_page(self):
        assert True

    def test_request_form_opens_from_request_page(self):
        assert True

    def test_request_form_opens_from_sidebar(self):
        assert True

    def test_request_form_opens_from_teammate_page(self):
        assert True

    def test_request_form_openst_from_team_page(self):
        assert True

    def test_feedback_form_opens_from_people_page(self):
        assert True

    def test_request_form_opens_from_people_page(self):
        assert True

if __name__ == '__main__':
    unittest.main()
