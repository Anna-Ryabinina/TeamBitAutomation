class Team(object):
    def __init__(self, team_data):
        self.id = team_data["id"]
        self.name = team_data["name"]