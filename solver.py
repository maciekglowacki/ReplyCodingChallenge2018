#TOTAL PROJECT SCORE

#AVERAGE LATENCY
def average_latency(project, regions, packages_count):
    services_count = 0
    for region, package_count in zip(regions,packages_count):
        print(region.latency)
        print(project.country)
        services_count += (sum(region.package_info.services_per_package.values()) * package_count)

def availability_index(project, regions, packages_count):
    services_count = []
    for region, package_count in zip(regions,packages_count):
        services_count.append(sum(region.package_info.services_per_package.values()) * package_count)
    
    q1 = sum(services_count)**2
    q2 = 0
    for x in services_count
        q2 += x.services_count**2
    availability_index_value = q1/q2
        





#AVAILABILITY INDEX

#SLA PENALTY 
