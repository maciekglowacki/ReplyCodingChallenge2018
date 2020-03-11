#TOTAL PROJECT SCORE

#AVERAGE LATENCY
def average_latency(project, regions, packages_count):
    services_count = 0
    for region, package_count in zip(regions,packages_count):
        print(region.latency)
        print(project.country)
        services_count += (sum(region.package_info.services_per_package.values()) * package_count)





#AVAILABILITY INDEX

#SLA PENALTY 
