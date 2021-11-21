import configparser

from CreateTasks import *
from HeuristicBinPacking import HeristicBinPacking

reader = configparser.ConfigParser()
reader.read(r"C:\Users\saiak\PycharmProjects\VimanTest\config.ini")
param = reader["Scheduling Parameters"]

n_tasks = int(param["n_tasks"])
max_exec_time = int(param["max_exec_time"])
config_ratio = float(param["config_ratio"])

if __name__ == '__main__':
    '''a = ['A',["S1","S2","Pathchar",50]]
    b = ['B',["S2","S3","Iperf",10]]
    c = ['C', ["S3", "S5", "H23", 30]]
    d = ['D', ["S5", "S1", "Iperf", 10]]

    t=[a,b,c,d] '''

    conflict_graph = createConfiggraph(n_tasks, config_ratio)
    tasks = createinputs(n_tasks, max_exec_time)

    HeristicBinPacking(tasks, conflict_graph)
