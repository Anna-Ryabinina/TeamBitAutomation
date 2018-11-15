class User(object):
    def __init__(self, user_data):
        self.name = user_data["first_name"]
        self.last_name = user_data["last_name"]
        self.email = user_data["email"]
        self.password = user_data["password"]
        self.id = user_data["id"]
        self.full_name = user_data["full_name"]