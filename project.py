class Project:
    def __init__(self,penalty,country,services):
        self.penalty = penalty
        self.country = country
        self.services = services

    def __str__(self):
        return f'Project penalty: {self.penalty}, Project country:{self.country}, Project services: {self.services}'