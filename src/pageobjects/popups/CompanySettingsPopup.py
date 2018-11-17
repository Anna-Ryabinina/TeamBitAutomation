from selene.api import *
from src.locators import *
from src.pages_url import *


class CompanySettingsPopup(object):

    def __init__(self):
        self.popup = s(by.xpath(COMPANY_SETTINGS_POPUP))
        self.close_button = s(by.xpath(COMPANY_SETTINGS_CLOSE_BUTTON))
        self.cancel_button = s(by.xpath(COMPANY_SETTINGS_CANCEL_BUTTON))
        self.save_button = s(by.xpath(COMPANY_SETTINGS_SAVE_BUTTON))
        self.add_value_button = s(by.xpath(COMPANY_SETTINGS_ADD_VALUE_BUTTON))

    def add_new_value(self, value_name):
        self.add_value_button.click()
        value = self.get_value_by_id(-1)
        value.type_text(value_name)
        return self.save()

    def delete_value_by_id(self, id):
        value = self.get_value_by_id(id)
        value.delete()
        return self.save()

    def delete_value_by_text(self, text):
        value = self.get_value_by_text(text)
        value.delete()
        return self.save()

    def close(self):
        self.close_button.click()
        return CompanySettingsPopup()

    def cancel(self):
        self.cancel_button.click()
        return CompanySettingsPopup()

    def save(self):
        self.save_button.click()
        return CompanySettingsPopup()

    def get_value_by_id(self, id):
        values = ss(COMPANY_SETTINGS_VALUE_BLOCK)
        if len(values) == 0:
            return None
        return ValueBlock(values[id])

    def get_value_by_text(self, text):
        values = ss(COMPANY_SETTINGS_VALUE_BLOCK)
        if len(values) == 0:
            return None
        for value in values:
            if text in value.element(by.xpath(COMPANY_SETTINGS_VALUE_NAME_INPUT)).text:
                return ValueBlock(value)
        return None


class ValueBlock(object):

    def __init__(self, value_from_list):
        self.icon_list = value_from_list.element(COMPANY_SETTINGS_VALUE_ICON_LIST)
        self.text_input = value_from_list.element(by.xpath(COMPANY_SETTINGS_VALUE_NAME_INPUT))
        self.delete_button = value_from_list.element(by.xpath(COMPANY_SETTINGS_VALUE_DELETE_BUTTON))
        self.value = value_from_list

    def type_text(self, text):
        self.text_input.set(text)

    def delete(self):
        self.delete_button.click()
