class Region:
    def __init__(self, name, latency, package_info):
        self.name = name
        self.latency = latency
        self.package_info = package_info

    def __str__(self):
        return f'Latency for each country:{self.latency}, Package information: {self.package_info}, Region name is: {self.name}'

    def __repr__(self):
        return self.__str__()
