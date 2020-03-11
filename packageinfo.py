class PackageInfo:
    def __init__(self, packages_count, package_cost, services_per_package):
        self.packages_count = packages_count
        self.package_cost = package_cost
        self.services_per_package = services_per_package

    def __str__(self):
        return f'Number of packages: {self.packages_count}, Cost of package: {self.package_cost}, Services: {self.services_per_package}'

    def __repr__(self):
        return self.__str__()