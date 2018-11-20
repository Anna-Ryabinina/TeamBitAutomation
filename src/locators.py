# SignUP and SignIn
SIGNUP_WITH_SLACK_BUTTON = '//*[text()="Sign up with Slack"]'
SIGNUP_WITH_GOOGLE_BUTTON = '//*[text()="Sign up with Google"]'
SIGNUP_EMAIL_TEXT_INPUT = '//*[@id="email"]'
SIGNUP_BUTTON = 'button[data-role="signup_button"]'
SIGNIN_HERE_LINK = '//*[text()="Sign in here"]'
SIGNUP_FOR_FREE_LINK = '//*[text()="Sign up for free"]'
SIGNIN_WITH_SLACK_BUTTON = '//*[text()="Sign in with Slack"]'
SIGNIN_WITH_GOOGLE_BUTTON = '//*[text()="Sign in with Google"]'
SIGNIN_EMAIL_TEXT_INPUT = '//*[@id="app"]/div/div/div/div/div[2]/div/div/fieldset/input'
SIGNIN_PASSWORD_TEXT_INPUT = '//*[@id="app"]/div/div/div/div/div[2]/div/div/div[4]/div[2]/div[1]/input'
SIGNIN_BUTTON = '//*[text()="Sign in to Teambit"]'
SIGNIN_FORGOT_LINK = '//*[text()="Forgot?"]'
SINGIN_EMAIL_ERROR_TEXT = '//*[@id="app"]/div/div/div/div/div[2]/div/div/fieldset/span/span'
SIGNIN_PASSWORD_ERROR_TEXT = '//*[@id="app"]/div/div/div/div/div[2]/div/div/div[4]/div[2]/div[2]/span'
SIGNUP_EMAIL_ERROR_TEXT = '//*[@id="app"]/div/div/div/div/div[2]/div/div/fieldset/span/span'
SIGN_UP_TO_TEAM_BUTTON = '//*[@id="app"]/div/div/div/div[2]/div/div/div[4]/button'

# OnboardingPopup appears after signup
ONBOARDING_POPUP = '.setup-account'
ONBOARDING_FIRST_NAME_TEXT_INPUT = '//*[@id="first_name"]'
ONBOARDING_LAST_NAME_TEXT_INPUT = '//*[@id="last_name"]'
ONBOARDING_COMPANY_TEXT_INPUT = '//*[@id="modal"]/div/div/div[2]/fieldset[2]/input'
ONBOARDING_JOB_TEXT_INPUT = '//*[@id="modal"]/div/div/div[2]/fieldset[3]/input'
ONBOARDING_PASSWORD_TEXT_INPUT = '//*[@id="password"]'
ONBOARDING_SMILE = '//*[@id="modal"]/div/div/div[1]/div[1]/a'
ONBOARDING_NEXT_BUTTON = '#continue_onboarding'
ONBOARDING_GUEST_EMAIL = '//*[@id="modal"]/div/div[1]/div[1]/table/tbody/tr/td[1]/fieldset/input'
ONBOARDING_ADD_ANOTHER_GUEST = '//*[@id="modal"]/div/div[1]/div[2]/div[1]/button'
ONBOARDING_FINISH_BUTTON = '.finish_onboarding'
ONBOARDING_SEND_BUTTON = '//*[@id="modal"]/div/div/div[1]/footer/div[2]/button'
ONBOARDING_INVITE_LINK = '//*[@id="modal"]/div/div[1]/div[2]/div[2]/div[1]/fieldset/input'
ONBOARDING_SURVEY_LIST = '.setup-surveys-modal-list'
ONBOARDING_SURVEY_BLOCK = '//*[@class="recurring-one-survey"]'
ONBOARDING_SURVEY_SET_LIVE_BUTTON = './/*[@class="recurring-one-survey-button-setup"]'
ONBOARDING_SURVEY_LIVE_BUTTON = './/*[@class="recurring-one-survey-question-setup"]'
ONBOARDING_SURVEY_TEXT = './/*[@class="recurring-one-survey-question-setup"]/b/span'

# Sidebar common elements
SIDEBAR_TEAMMATE = '.left-panel-users-list-user'
SIDEBAR_TEAMMATE_NAME = ".//a"
SIDEBAR_TEAMMATE_FEEDBACK_BUTTON = '.new-small-icon'
SIDEBAR_TEAMMATE_REQUEST_BUTTON = '.ask-small-icon'
SIDEBAR_INVITE_LINK = '.left-panel-users-list-invite'

        # FeedbackPage
FEEDBACK_LOGO = '#app > div > header > div.logo'
FEEDBACK_SEND_FEEDBACK_BUTTON = '//*[@id="app"]/div/div[1]/div/button'
FEEDBACK_MENU_ALL_LINK = '//*[@id="app"]/div/div[2]/nav/a[2]'
FEEDBACK_MENU_SENT_LINK = '//*[@id="app"]/div/div[2]/nav/a[7]'
FEEDBACK_MENU_TO_YOU_LINK = '//*[@id="app"]/div/div[2]/nav/a[3]'
FEEDBACK_MENU_ADDED_TO_PRAISE = '//*[@id="app"]/div/div[2]/nav/a[4]'
FEEDBACK_MENU_VIA_SURVEYS_LINK = '//*[@id="app"]/div/div[2]/nav/a[5]'
FEEDBACK_MENU_VIA_REVIEWS_LINK = '//*[@id="app"]/div/div[2]/nav/a[6]'
FEEDBACK_MENU_FLAGGED = '//*[@id="app"]/div/div[2]/nav/a[8]'
FEEDBACK_SUCCESSFULLY_SENT_MESSAGE = ''
FEEDBACK_BLOCK = '.one-feedback'
FEEDBACK_POPUP = '//*[@id="modal"]/div/div'

        # FeedbackPopup
FEEDBACK_POPUP_FEEDBACK_TAB = '//*[@id="modal"]//*[text()="Send feedback"]'
FEEDBACK_POPUP_REQUEST_TAB = '//*[@id="modal"]//*[text()="Request feedback"]'
FEEDBACK_POPUP_RECIPIENTS_TEXT_INPUT = '#modal > div > div > div.feedback-modal-receivers > div.teambit-multiselect > div > div > input[type="text"]'
FEEDBACK_POPUP_RECIPIENTS_NAME_LIST = '//*[@id="modal"]/div/div/div[1]/div[1]/div/div[1]'
FEEDBACK_POPUP_RECIPIENT_ADDED = '#modal > div > div > div.feedback-modal-receivers > div.teambit-multiselect > div > div.value > span'
FEEDBACK_POPUP_FEEDBACK_TEXT_INPUT = '//*[@id="modal"]/div/div/div[2]/div/div/textarea'
FEEDBACK_POPUP_FROM_TEXT_INPUT = '//*[@id="modal"]/div/div/div[2]/div/div/textarea'
FEEDBACK_POPUP_REQUEST_TEXT_INPUT = '//*[@id="modal"]/div/div/div[2]/div/div/textarea'
FEEDBACK_POPUP_CLOSE_ICON = '//*[@id="modal"]/div/div/button'
FEEDBACK_POPUP_SEND_FEEDBACK_BUTTON = '//*[@id="modal"]/div/div/footer/button'
FEEDBACK_POPUP_SEND_REQUEST_BUTTON = '//*[@id="modal"]/div/div/footer/button'
FEEDBACK_POPUP_ADD_VALUE_ICON = '//*[@id="modal"]/div/div/footer/div/div[1]/i'
FEEDBACK_POPUP_VALUE_TO_CHOOSE = '//*[@class="emojione"]'
FEEDBACK_POPUP_VALUE_PIC_ADDED = '#modal > div > div > div.b-panel__entry > div > div.new-feedback-modal-value > div > div:nth-child(2) > span > svg > use'
FEEDBACK_POPUP_FEEDBACK_TEMPLATE_ICON = '//*[@id="modal"]/div/div/footer/div/div[3]/i'
FEEDBACK_POPUP_REQUEST_TEMPLATE_ICON = '//*[@id="modal"]/div/div/footer/div/div/i'
FEEDBACK_POPUP_TEMPLATE_TO_CHOOSE = '//*[@id="modal"]/div/div/footer/div/div[1]/div/div/section'
FEEDBACK_POPUP_MAKE_PUBLIC_ICON = '//*[@id="modal"]/div/div/footer/div/div[2]/i'

        # FeedbackBlock
FEEDBACK_BLOCK_VALUE_ICON = ".//*[@class='emojione']"
FEEDBACK_BLOCK_FEEDBACK_TEXT = './div[2]/div/div[1]/pre/span'
FEEDBACK_BLOCK_ADD_TO_PRAISE_LINK = './/*[@data-role="praise-feedback"]'
FEEDBACK_BLOCK_PEOPLE_NAME = '.one-feedback-people'
FEEDBACK_BLOCK_FLAGGED_LINK = './/*[@data-role="flag-feedback"]'
FEEDBACK_BLOCK_LIKE_ICON = './/*[@data-role="like-feedback"]'
FEEDBACK_BLOCK_DATE = './div[1]/span[2]'
FEEDBACK_BLOCK_COMMENT_ICON = './/*[@data-role="comment-feedback"]'
FEEDBACK_BLOCK_MORE_LINK = '.additional-feedback-buttons'
FEEDBACK_BLOCK_EDIT_LINK = '.icon edit-icon'
FEEDBACK_BLOCK_DELETE_LINK = '.icon remove-icon'


        # RequestPage
REQUEST_MENU_PENDING_REQUESTS = '//*[@id="app"]/div/div[2]/nav/a[1]'
REQUEST_MENU_SENT_REQUESTS = '//*[@id="app"]/div/div[2]/nav/a[2]'
REQUEST_MENU_RESOLVED_REQUESTS = '//*[@id="app"]/div/div[2]/nav/a[3]'
REQUEST_BLOCK = '.one-request'
REQUEST_REQUESTS_FEEDBACK_BUTTON = '//*[@id="app"]/div/div[1]/div/button'

        # RequestBlock
REQUEST_BLOCK_DATE = './div[1]/span[2]'
REQUEST_BLOCK_TEXT = './div[2]/span'
REQUEST_BLOCK_SEND_FEEDBACK_BUTTON = './/*[@class="icon send-feedback"]'
REQUEST_BLOCK_DISMISS_LINK = './/*[@class="icon revoke-blue-icon"]'

        # SurveyPage
SURVEY_CREATE_NEW_SURVEY_BUTTON     = '//*[@id="app"]/div/div[1]/div/button'
SURVEY_MENU_SURVEY     = '//*[@id="app"]/div/div[2]/nav/a'
SURVEY_BLOCK     = '.recurring-one-survey'
SURVEY_BLOCK_TITLE     = '.recurring-one-survey-question'
SURVEY_BLOCK_PAUSED_STATUS     = '.recurring-one-survey-label-paused'
SURVEY_BLOCK_AUTHOR     = '.recurring-one-survey-author'
SURVEY_INFO_PAUSE_BUTTON     = '//*[@id="app"]/div/div[1]/div[1]/header/div[3]/button'
SURVEY_INFO_BACK_BUTTON     = '//*[@id="app"]/div/div[1]/div[1]/a'
SURVEY_INFO_EDIT_BUTTON     = '//*[@id="app"]/div/div[1]/div[1]/header/div[2]/button'
SURVEY_POPUP     = '//*[@id="modal01"]'

        # SurveyPopup
SURVEY_POPUP_CLOSE_BUTTON     = '//*[@id="modal"]/div/header/button'
SURVEY_POPUP_HEADER     = '//*[@id="modal01"]/header/b'
SURVEY_POPUP_CREATE_EMPTY_SURVEY_BUTTON     = '//*[@id="modal01"]/div/div/div/div[1]/div[2]'
SURVEY_POPUP_CREATE_SURVEY_BUTTON     = '//*[@id="modal01"]/div/div/div/div[2]/div[2]'
SURVEY_POPUP_OR_CHOOSE_ANOTHER_TEMPLAY_LINK     = '//*[@id="modal"]/div/header/p/a'
SURVEY_POPUP_SURVEY_NAME_TEXT_INPUT     = '//*[@id="modal"]/div/div/div[1]/div[1]/div[1]/fieldset/input'
SURVEY_POPUP_QUESTION_SECTION     = './/*[@data-role="survey-question"]'
SURVEY_POPUP_QUESTION_TEXT_INPUT     = './/*[@data-role="survey-question-text"]'
SURVEY_POPUP_QUESTION_RATING_OPTION_BUTTON     = './/*[@data-role="survey-question-type-range"]'
SURVEY_POPUP_QUESTION_TEXT_OPTION_BUTTON     = './/*[@data-role="survey-question-type-text"]'
SURVEY_POPUP_QUESTION_PUBLIC_OPTION_BUTTON     = './/*[@data-role="survey-question-publicity-public"]'
SURVEY_POPUP_QUESTION_ANONYMOUS_OPTION_BUTTON     = './/*[@data-role="survey-question-publicity-anon"]'
SURVEY_POPUP_ADD_QUESTION_BUTTON     = '//*[@id="modal"]/div/div/div[1]/div[1]/div[3]/button'
SURVEY_POPUP_REMOVE_QUESTION_BUTTON     = './/*[@data-role="survey-remove-question"]'
SURVEY_POPUP_SETTING_HOW_OFTEN_LIST     = ''
SURVEY_POPUP_SETTING_HOW_OFTEN_EVERY_ITEM     = ''
SURVEY_POPUP_SETTING_DAYS_LIST     = ''
SURVEY_POPUP_SETTING_DAYS_EVERY_ITEM     = ''
SURVEY_POPUP_SETTING_TEAMMATE_TEXT_INPUT     = '//*[@class="teambit-multiselect-selector-container"]/input'
SURVEY_POPUP_CREATE_BUTTON     = '//*[@id="modal"]/div/div/div[1]/div[2]/div/button'
SURVEY_POPUP_CHOOSE_DATE_TIME_BUTTON = ".react-datepicker-wrapper"
SURVEY_POPUP_RUN_NOW_BUTTON = "//*[@id=\"modal\"]/div/div/div[1]/div[2]/div/span/button"
SURVEY_POPUP_WHO_REQUEST_FROM_INPUT = '//*[@id="modal"]/div/div/div[1]/div[1]/div[6]/div/div/div'
SURVEY_POPUP_WHO_ABLE_TO_SEE_INPUT = '//*[@id="modal"]/div/div/div[1]/div[1]/div[7]/div/div/div/input'

MAIN_MENU_FEEDBACK = ''
MAIN_MENU_REQUESTS = ''
MAIN_MENU_SURVEYS = ''
MAIN_MENU_REVIEWS = ''


TEAMMATE_EDIT_BUTTON = '//*[@id="app"]/div/div[3]/div[2]/div/section[2]/div/div[6]/button'
TEAMMATE_SEND_FEEDBACK_BUTTON = '//*[@id="app"]/div/div[3]/div[2]/div/section[2]/div/div[6]/button[1]'
TEAMMATE_REQUEST_FEEDBACK_BUTTON = '//*[@id="app"]/div/div[3]/div[2]/div/section[2]/div/div[6]/button[2]'

EDIT_PROFILE_FIRST_NAME_INPUT = '//*[@id="modal"]/div/div/div[3]/div[1]/div[1]/fieldset/input'
EDIT_PROFILE_LAST_NAME_INPUT = '//*[@id="modal"]/div/div/div[3]/div[1]/div[2]/fieldset/input'
EDIT_PROFILE_BIO_INPUT = '//*[@id="modal"]/div/div/div[3]/div[2]/div[1]/textarea'
EDIT_PROFILE_JOB_INPUT = '//*[@id="modal"]/div/div/div[3]/fieldset[1]/input'
EDIT_PROFILE_YOU_MANAGE_INPUT = '//*[@id="modal"]/div/div/div[3]/div[3]/div/div/input'
EDIT_PROFILE_YOU_REPORT_TO_INPUTE = '//*[@id="modal"]/div/div/div[3]/div[5]/div/div/input'
EDIT_PROFILE_YOU_WORK_WITH_INPUT = '//*[@id="modal"]/div/div/div[3]/div[5]/div/div/input'
EDIT_PROFILE_LOCATION_INPUT = '//*[@id="modal"]/div/div/div[3]/fieldset[2]/input'
EDIT_PROFILE_PHONE_INPUT = '//*[@id="modal"]/div/div/div[3]/fieldset[3]/input'
EDIT_PROFILE_SLACK_INPUT = '//*[@id="modal"]/div/div/div[3]/fieldset[4]/input'
EDIT_PROFILE_SKYPE_INPUTED = '//*[@id="modal"]/div/div/div[3]/fieldset[5]/input'
EDIT_PROFILE_EMAIL_INPUTED = '//*[@id="modal"]/div/div/div[3]/fieldset[6]/input'
EDIT_PROFILE_TWITTER_INPUT = '//*[@id="modal"]/div/div/div[3]/fieldset[7]/input'
EDIT_PROFILE_FACEBOOK_INPUT = '//*[@id="modal"]/div/div/div[3]/fieldset[8]/input'
EDIT_PROFILE_LINKEDIN_INPUT = '//*[@id="modal"]/div/div/div[3]/fieldset[9]/input'
EDIT_PROFILE_INSTAGRAM_INPUT = '//*[@id="modal"]/div/div/div[3]/fieldset[10]/input'
EDIT_PROFILE_CANCEL_BUTTON = '//*[@id="modal"]/div/footer/button[2]'
EDIT_PROFILE_SAVE_BUTTON = '//*[@id="modal"]/div/footer/button[1]'
EDIT_PROFILE_CLOSE_BUTTON = '//*[@id="modal"]/div/button'
EDIT_PROFILE_POPUP = '//*[@id="modal"]/div'

COMPANY_SETTINGS_POPUP = '//*[@id="modal"]/div'
COMPANY_SETTINGS_CLOSE_BUTTON = '//*[@id="modal"]/div/button'
COMPANY_SETTINGS_CANCEL_BUTTON = '//*[@id="modal"]/div/footer/button[2]'
COMPANY_SETTINGS_SAVE_BUTTON = '//*[@id="modal"]/div/footer/button[1]'
COMPANY_SETTINGS_NAME_INPUT = '//*[@id="modal"]/div/div/div[1]/fieldset/input'
COMPANY_SETTINGS_VALUE_BLOCK = '.o-editable-value-row'
COMPANY_SETTINGS_VALUE_ICON_LIST = '.selectbox'
COMPANY_SETTINGS_VALUE_NAME_INPUT = './div[2]/input'
COMPANY_SETTINGS_VALUE_DELETE_BUTTON = './div[3]/button'
COMPANY_SETTINGS_ADD_VALUE_BUTTON = '//*[@id="modal"]/div/div/div[2]/div/button'

PEOPLE_INVITE_BUTTON = '//*[@id="app"]/div/div[1]/div/button'
PEOPLE_TEAMMATE_ROW = '.one-user'
PEOPLE_TEAMMATE_NAME_LINK = '.username'
PEOPLE_TEAMMATE_SEND_FEEDBACK_BUTTON = './td[2]/button'
PEOPLE_TEAMMATE_REQUEST_FEEDBACK_BUTTON = './td[3]/button'
PEOPLE_TEAMMATE_MAKE_ADMIN_BUTTON = './td[4]/button[1]'
PEOPLE_TEAMMATE_MAKE_USER_BUTTON = './td[4]/button[1]'
PEOPLE_TEAMMATE_DELETE_USER = './td[4]/button[2]'

TEAMS_CREATE_NEW_BUTTON = '//*[@id="app"]/div/div[1]/div/button'
TEAM_ROW = '.table-row'
TEAM_SEND_FEEDBACK_BUTTON = './td[3]/button[1]'
TEAM_REQUEST_FEEDBACK_BUTTON = './td[3]/button[2]'
TEAM_EDIT_BUTTON = './td[3]/button[3]'
TEAM_LEAVE_BUTTON = './td[4]/button'
TEAM_JOIN_BUTTON = './td[4]/button'
TEAM_NAME = './td[2]/div/div[1]/b'







