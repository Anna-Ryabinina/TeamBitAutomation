import unittest
import time
from src.pages.pages.SignUpPage import SignUpPage
from src.pages.pages.FeedbackPage import FeedbackPage
from src.pages.popups.OnboardingPopup import *
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

        survey_on_onboarding = OnboardingPopup().get_survey_block_by_id(0)

        txt_of_survey = survey_on_onboarding.text

        survey_on_onboarding.set_live_button.click()

        survey_on_onboarding = OnboardingPopup().get_survey_block_by_text(txt_of_survey)

        survey_on_onboarding.live_button.should(be.visible)

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
