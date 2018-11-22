
class SurveyPayload(object):

    def __init__(self, title=''):
        self.questions = []
        self.title = title
        self.schedule = {"time": 9, "day": 1, "period": "weekly", "is_active": True, "timezone": "Europe/Kiev"}
        self.next_run_date = ''
        self.receivers = ['all']
        self.viewers = ['all']
        self.user_id = None
        self.template = None
        self.show_to_all = None
        self.is_recurrent = None
        self.is_active = None
        self.cycles_count = None
        self.organisation_id = None
        self.is_viewed = None
        self.id = None
        self.created_at = None
        self.ask_everyone = None

    def add_text_question(self, question_text, is_anonymous=False):
        self.questions.append(
            {"text": question_text,
             "type": 2,
             "isAnonymous": is_anonymous}
        )
        return self

    def add_rating_question(self, question_text, is_anonymous=False):
        self.questions.append(
            {"text": question_text,
             "type": 1,
             "isAnonymous": is_anonymous}
        )
        return self

    def set_schedule(self, period='dayly', day=1, time=9, is_active=True):
        self.schedule = {"period": period, "day": day, "time": time, "is_active": is_active, "timezone": "Europe/Kiev"}

    def set_receivers(self, users):
        r = [user.id for user in users]
        self.receivers = r
        return self

    def set_viewers(self, users):
        v = [user.id for user in users]
        self.viewers = v
        return self

    def set_title(self, title):
        self.title = title
        return self

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

    def generate_new_survey_data_for_date(self, date):
        return {
            "isEditing":False,
            "name":self.title,
            "questions":self.questions,
            "schedule":self.schedule,
            "nextRunDate":date,
            "valid":True,
            "runNow":False,
            "showCalendar":False,
            "receivers":self.receivers,
            "viewers":self.viewers,
            "time":9}

    def generate_from_json(self, json):
        self.title = json['name']
        self.viewers = json['viewers']
        self.user_id = json['user_id']
        self.template = json['template']
        self.show_to_all = json['show_to_everyone']
        self.schedule = json['schedule']
        self.receivers = json['receivers']
        self.questions = json['questions']
        self.organisation_id = json['organization_id']
        self.title = json['name']
        self.is_viewed = json['is_viewed']
        self.is_active = json['schedule']['is_active']
        self.id = json['id']
        self.created_at = json['created_at']
        self.ask_everyone = json['ask_everyone']
        return self




