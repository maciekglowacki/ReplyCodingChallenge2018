from parser import read_input
from solver import average_latency
if __name__ == '__main__':
    providers, projects = read_input()
    average_latency(projects[0],providers[0].regions,[50,20])

