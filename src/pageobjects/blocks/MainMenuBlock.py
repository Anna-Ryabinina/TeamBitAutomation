from selene.api import *
from src.locators import *


class MainMenuBlock(object):
    def __init__(self):
        self.feedback = s(MAIN_MENU_FEEDBACK)
        self.requests = s(MAIN_MENU_REQUESTS)
        self.surveys = s(MAIN_MENU_SURVEYS)
        self.reviews = s(MAIN_MENU_REVIEWS)