import datetime


class FeedbackPayload(object):
    def __init__(self, recipient_array, shared=False, value=None):
        self.recipient = recipient_array
        self.shared = shared
        self.value = value

    def get_recepient_ids_array(self):
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
        fb = {
            "recepients":self.get_recepient_ids_array(),
            "value" : self.value,
            "text": self.return_feedback_text(),
            "is_shared":self.shared
        }
        return FeedbackData(fb)

    def return_feedback_text(self):
        D = datetime.date.today().strftime('%b %d')
        st = self.is_public_str() + D + " to " + self.get_recipient_names_str()
        return st


class FeedbackData(object):
    def __init__(self, json):
        self.json = json
        self.text = json["text"]
        self.is_shared = json["is_shared"]


