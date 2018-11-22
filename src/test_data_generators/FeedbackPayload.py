
class FeedbackPayload(object):

    def __init__(self):
        self.recipients = None
        self.value = None
        self.date = None
        self.text = None
        self.is_anonymous = None
        self.id = None
        self.user_id = None
        self.likes_count = None
        self.comments_count = None
        self.is_shared = None
        self.organization_id = None
        self.to_everyone = None
        self.emails = None
        self.type = None
        self.variant = None
        self.parent_id = None
        self.target_id = None
        self.integrations = None
        self.question_id = None
        self.run_id = None
        self.next_id = None
        self.is_edited = None
        self.users = None
        self.teams = None
        self.state = None
        self.json_for_send = None

    def get_recipient_names_str(self, recipients):
        n = ""
        for r in recipients:
            n = n + r.name
        return n

    def generate_feedback_to_send(self, recipients, text, is_shared=False, value=None):
        self.recipients = recipients
        self.is_shared = is_shared
        self.value = value
        shared_str = 'private'
        if is_shared:
            shared_str = 'public'
        self.text = text + shared_str + ' feedback to ' + self.get_recipient_names_str(recipients)
        self.json_for_send = {
            "recepients": [r.id for r in self.recipients],
            "value" : self.value,
            "text": self.text,
            "is_shared": self.is_shared
        }
        return self

    def generate_feedback_from_json(self, json):
        self.value = json['value']
        self.is_shared = json['is_shared']
        self.date = json['date']
        self.text = json['text']
        self.is_anonymous = json['is_anonymous']
        self.id = json['id']
        self.user_id = json['user_id']
        self.likes_count = json['likes_count']
        self.comments_count = json['comments_count']
        self.is_shared = json['is_shared']
        self.organization_id = json['organization_id']
        self.to_everyone = json['to_everyone']
        self.emails = json['emails']
        self.type = json['type']
        self.variant = json['variant']
        self.parent_id = json['parent_id']
        self.target_id = json['target_id']
        self.integrations = json['integrations']
        self.question_id = json['question_id']
        self.run_id = json['run_id']
        self.next_id = json['next_id']
        self.is_edited = json['is_edited']
        self.users = json['users']
        self.teams = json['teams']
        self.state = json['state']
        return self



