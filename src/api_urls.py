from selene.api import *

HOST_NAME = config.base_url
SIGNUP_API_URL = ""
LOGIN_API_URL = HOST_NAME + "/api/users/auth"
SEND_FEEDBACK_API_URL = HOST_NAME + "/api/feedback"
SEND_REQUEST_API_URL = HOST_NAME + "/api/requests"
CREATE_SURVEY_URL = HOST_NAME + "/api/surveys/"
GET_SURVEYS_URL = HOST_NAME + "/api/surveys/"
GET_ALL_FEEDBACK_URL = HOST_NAME + "/api/feedback/all"
