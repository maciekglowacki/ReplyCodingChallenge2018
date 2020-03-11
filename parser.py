from region import Region
from packageinfo import PackageInfo
from provider import Provider
from project import Project

providers_count, services_count, countries_count, projects_count = [
    int(x) for x in input().split()]

services = [service for service in input().split()]
countries = [country for country in input().split()]
providers = []
projects = []


for provider in range(providers_count):
    provider_name, regions_count = input().split()
    regions = []
    for region in range(int(regions_count)):
        region_name = input()
        line = input().split()
        packages_count = line[0]
        package_cost = line[1]
        services_per_package = [int(x) for x in line[2:]]
        latency = [int(x) for x in input().split()]
        regions.append(Region(region_name, latency, PackageInfo(packages_count, package_cost, services_per_package)))
    providers.append(Provider(provider_name,regions))




for project in range(projects_count):
    line = input().split()
    penalty = int(line[0])
    country = line[1]
    services = [int(x) for x in line[2:]]
    projects.append(Project(penalty,country,services))
    

print(projects[0])
