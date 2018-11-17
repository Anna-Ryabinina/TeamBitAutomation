import datetime


class RequestPayload(object):
    def __init__(self, recipient_array, d=None, text=None):
        self.recipient = recipient_array
        self.text = text
        self.d = d

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

    def generate_request_data(self):
        if self.text is None:
            if self.d is None:
                self.d = datetime.datetime.today().strftime('%c')
            self.text = self.d + ' test request to' + self.get_recipient_names_str()
        rq = {
            "recepients": self.get_recipient_ids_array(),
            "text": self.text
        }
        return RequestData(rq)


class RequestData(object):
    def __init__(self, json):
        self.json = json
        self.text = json["text"]


