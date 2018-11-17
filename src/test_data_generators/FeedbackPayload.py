import datetime


class FeedbackPayload(object):

    def __init__(self, recipient_array, text_prefix='', shared=None, value=None):
        self.recipient = recipient_array
        self.value = value
        self.text = text_prefix
        self.shared = shared

    def get_recipient_ids_array(self):
        i = []
        for r in self.recipient:
            i.append(r.id)
        return i

    def get_recipient_names_str(self):
        n = ""
        for r in self.recipient:
            n = n + r.name
        return n

    def is_public_str(self):
        if self.shared:
            return "public "
        else:
            return "private "

    def generate_feedback_data(self):
        text = self.text + self.is_public_str() + ' feedback to ' + self.get_recipient_names_str()
        fb = {
            "recepients":self.get_recipient_ids_array(),
            "value" : self.value,
            "text": text,
            "is_shared": self.shared
        }
        return FeedbackData(fb)


class FeedbackData(object):
    def __init__(self, json):
        self.json = json
        self.text = json["text"]
        self.is_shared = json["is_shared"]


