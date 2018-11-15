import unittest
import time
from selene.api import *
from src.test_data import *
from src.pages_url import *
from src.test_data_generators.User import User
from src.pages.LogInPage import LoginPage
from src.pages.SignUpPage import SignUpPage
from src.pages.FeedbackPage import FeedbackPage
from src.pages.OnboardingPopup import *
from tests.BaseTest import BaseTest


class OnboardingTests(BaseTest):

    def test_onboarding_popup_elements(self):
        test_email = 'autotest' + str(time.time()) + '@test.com'
        SignUpPage().open().signup(test_email)
        (OnboardingPopup()
         .popup.should(be.visible))
        (OnboardingPopup()
         .fill_account_info()
         .survey_list.should(be.visible))
        txt = SurveyBlockOnOnboarding(OnboardingPopup().survey_blocks[0]).text
        (SurveyBlockOnOnboarding(OnboardingPopup().survey_blocks[0])
         .set_live_button.click())
        (OnboardingPopup()
         .get_survey_block_by_text(txt)
         .live_button.should(be.visible))
        (OnboardingPopup()
         .click_next()
         .click_smile_icon()
         .click_next()
         .click_add_guest()
         .guest_inputs.should(have.size(2)))
        OnboardingPopup().click_finish()
        FeedbackPage().logo.should(be.visible)


if __name__ == '__main__':
    unittest.main()
