from selene.api import *
from src.locators import *


class OnboardingPopup(object):
    def __init__(self):
        self.popup = s(ONBOARDING_POPUP)
        self.first_name_input = s(by.xpath(ONBOARDING_FIRST_NAME_TEXT_INPUT))
        self.last_name_input = s(by.xpath(ONBOARDING_LAST_NAME_TEXT_INPUT))
        self.job_input = s(by.xpath(ONBOARDING_JOB_TEXT_INPUT))
        self.password_input = s(by.xpath(ONBOARDING_PASSWORD_TEXT_INPUT))
        self.company_input = s(by.xpath(ONBOARDING_COMPANY_TEXT_INPUT))
        self.smile_icon = s(by.xpath(ONBOARDING_SMILE))
        self.next_button = s(ONBOARDING_NEXT_BUTTON)
        self.guest_inputs = ss(by.xpath(ONBOARDING_GUEST_EMAIL))
        self.add_guest_button = s(by.xpath(ONBOARDING_ADD_ANOTHER_GUEST))
        self.invite_link = s(by.xpath(ONBOARDING_INVITE_LINK))
        self.survey_list = s(ONBOARDING_SURVEY_LIST)
        self.survey_blocks = ss(by.xpath(ONBOARDING_SURVEY_BLOCK))
        self.finish_button = s(by.xpath(ONBOARDING_FINISH_BUTTON))
        self.send_invite_button = s(by.xpath(ONBOARDING_SEND_BUTTON))

    def get_survey_block_by_text(self, text):
        surveys = self.survey_blocks
        if len(surveys) == 0:
            return None
        else:
            for survey in surveys:
                if text in survey.element(by.xpath(ONBOARDING_SURVEY_TEXT)).text:
                    return SurveyBlockOnOnboarding(survey)
            return None

    def get_survey_block_by_id(self, id):
        surveys = self.survey_blocks
        if len(surveys) == 0 or len(surveys) <= id:
            return None
        else:
            return SurveyBlockOnOnboarding(surveys[id])

    def fill_account_info(self):
        self.first_name_input.set('test')
        self.last_name_input.set('test')
        self.company_input.set('test')
        self.job_input.set('test')
        self.password_input.set('123456')
        self.next_button.click()
        return OnboardingPopup()

    def click_next(self):
        self.next_button.click()
        return OnboardingPopup()

    def click_smile_icon(self):
        self.smile_icon.click()
        return OnboardingPopup()

    def click_add_guest(self):
        self.add_guest_button.click()
        return OnboardingPopup()

    def click_finish(self):
        self.finish_button.click()
        return OnboardingPopup()


class SurveyBlockOnOnboarding(object):
    def __init__(self, survey):
        self.text = survey.element(by.xpath(ONBOARDING_SURVEY_TEXT)).text
        self.set_live_button = survey.element(by.xpath(ONBOARDING_SURVEY_SET_LIVE_BUTTON))
        self.live_button = survey.element(by.xpath(ONBOARDING_SURVEY_LIVE_BUTTON))
        self.survey = survey

    def click_live_button(self):
        self.live_button.click()
        return SurveyBlockOnOnboarding(self.survey)

    def click_set_live_button(self):
        self.set_live_button.click()
        return SurveyBlockOnOnboarding(self.survey)

