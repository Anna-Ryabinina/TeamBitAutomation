import datetime

class SurveyPayload(object):

    def __init__(self, title=''):
        self.questions = []
        self.title = title
        self.schedule = {"time": 9, "day": 1, "period": "weekly", "is_active": True, "timezone": "Europe/Kiev"}
        self.next_run_date = ''
        self.receivers = ['all']
        self.viewers = ['all']

    def add_text_question(self, question_text, is_anonymous=False):
        self.questions.append(
            {"text": question_text,
             "type": 2,
             "isAnonymous": is_anonymous}
        )

    def set_schedule(self, period='dayly', day=1, time=9):
        self.schedule = {"period": period, "day": day, "time": time, "timezone": "Europe/Kiev"}

    def set_receivers(self, users):
        r = [user.id for user in users]
        self.receivers = r

    def set_viewers(self, users):
        v = [user.id for user in users]
        self.viewers = v

    def generate_new_survey_data_run_now(self):
        return {
            "isEditing": False,
            "name": self.title,
            "questions": self.questions,
            "schedule": self.schedule,
            "nextRunDate": "18-11-2018 21:52",
            "valid": True,
            "runNow": True,
            "showCalendar": False,
            "receivers": self.receivers,
            "viewers": self.viewers,
            "time": 9}

