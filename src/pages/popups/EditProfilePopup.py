from selene.api import *
from src.locators import *
from src.test_data_generators.User import User
from src.test_data import *
from pynput.keyboard import Controller, Key


class EditProfilePopup(object):

    def __init__(self):
        self.close_button = s(by.xpath(EDIT_PROFILE_CLOSE_BUTTON))
        self.cancel_button = s(by.xpath(EDIT_PROFILE_CANCEL_BUTTON))
        self.save_button = s(by.xpath(EDIT_PROFILE_SAVE_BUTTON))
        self.first_name_input = s(by.xpath(EDIT_PROFILE_FIRST_NAME_INPUT))
        self.last_name_input = s(by.xpath(EDIT_PROFILE_LAST_NAME_INPUT))
        self.job_input = s(by.xpath(EDIT_PROFILE_JOB_INPUT))
        self.bio_input = s(by.xpath(EDIT_PROFILE_BIO_INPUT))
        self.you_manage_input = s(by.xpath(EDIT_PROFILE_YOU_MANAGE_INPUT))
        self.you_report_to_input = s(by.xpath(EDIT_PROFILE_YOU_REPORT_TO_INPUTE))
        self.you_work_with_input = s(by.xpath(EDIT_PROFILE_YOU_WORK_WITH_INPUT))
        self.location_input = s(by.xpath(EDIT_PROFILE_LOCATION_INPUT))
        self.email_input = s(by.xpath(EDIT_PROFILE_EMAIL_INPUTED))
        self.phone_input = s(by.xpath(EDIT_PROFILE_PHONE_INPUT))
        self.slack_input = s(by.xpath(EDIT_PROFILE_SLACK_INPUT))
        self.skype_input = s(by.xpath(EDIT_PROFILE_SKYPE_INPUTED))
        self.twitter_input = s(by.xpath(EDIT_PROFILE_TWITTER_INPUT))
        self.facebook_input = s(by.xpath(EDIT_PROFILE_FACEBOOK_INPUT))
        self.linkedin_input = s(by.xpath(EDIT_PROFILE_LINKEDIN_INPUT))
        self.instagram_input = s(by.xpath(EDIT_PROFILE_INSTAGRAM_INPUT))
        self.popup = s(by.xpath(EDIT_PROFILE_POPUP))

    def fill_all_inputs_and_save(self):
        keyboard = Controller()
        teammate = User(user_4).full_name
        self.first_name_input.set('test')
        self.last_name_input.set('test')
        self.job_input.set('test')
        self.bio_input.set('test')
        self.you_manage_input.set(teammate)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        self.you_report_to_input.set(teammate)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        self.you_work_with_input.set(teammate)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        self.location_input.set('test')
        self.phone_input.set('test')
        self.slack_input.set('test')
        self.skype_input.set('test')
        self.email_input.set('test')
        self.twitter_input.set('test')
        self.facebook_input.set('test')
        self.linkedin_input.set('test')
        self.instagram_input.set('test')
        self.save_button.click()
        return EditProfilePopup()

    def close(self):
        self.close_button.click()
        return EditProfilePopup()

    def cancel(self):
        self.cancel_button.click()
        return EditProfilePopup()

    def save(self):
        self.save_button.click()
        return EditProfilePopup()

    def type_first_name(self, text):
        self.first_name_input.set(text)
        return EditProfilePopup()

    def type_last_name(self, text):
        self.last_name_input.set(text)
        return EditProfilePopup()

    def type_job(self, text):
        self.job_input.set(text)
        return EditProfilePopup()

    def type_bio(self, text):
        self.bio_input.set(text)
        return EditProfilePopup()

    def type_location(self, text):
        self.location_input.set(text)
        return EditProfilePopup()

    def type_phone(self, text):
        self.phone_input.set(text)
        return EditProfilePopup()

    def type_slack(self, text):
        self.slack_input.set(text)
        return EditProfilePopup()

    def type_skype(self, text):
        self.skype_input.set(text)
        return EditProfilePopup()

    def type_facebook(self, text):
        self.facebook_input.set(text)
        return EditProfilePopup()

    def type_instagram(self, text):
        self.instagram_input.set(text)
        return EditProfilePopup()

    def type_linkedin(self, text):
        self.linkedin_input.set(text)
        return EditProfilePopup()

    def type_twitter(self, text):
        self.twitter_input.set(text)
        return EditProfilePopup()

    def type_email(self, text):
        self.email_input.set(text)
        return EditProfilePopup()

    def type_whom_you_work_with(self, name):
        keyboard = Controller()
        self.you_work_with_input.set(name)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        return EditProfilePopup()

    def type_whom_you_report_to(self, name):
        keyboard = Controller()
        self.you_report_to_input.set(name)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        return EditProfilePopup()

    def type_who_you_manage(self, name):
        keyboard = Controller()
        self.you_manage_input.set(name)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        return EditProfilePopup()
