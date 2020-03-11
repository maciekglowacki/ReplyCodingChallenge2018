class Provider:
    def __init__(self, name, regions):
        self.name = name
        self.regions = regions

    def __str__(self):
        return f'Provider name is: {self.name} and regions: {self.regions}'

    def __repr__(self):
        return self.__str__()