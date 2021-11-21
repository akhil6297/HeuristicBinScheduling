import configparser
import random

reader = configparser.ConfigParser()
reader.read(r"C:\Users\saiak\PycharmProjects\VimanTest\config.ini")
param = reader["Scheduling Parameters"]


def createConfiggraph(n_tasks, config_ratio):
    edges = n_tasks * (n_tasks - 1) // 2
    n_conflicts = int(edges * config_ratio)
    tasks = {}
    print(n_conflicts)
    for i in range(n_conflicts):
        index = random.randint(1, n_tasks)
        if index in tasks.keys():
            v = random.randint(1, n_tasks)
            while (v == index or v in tasks[index]):
                v = random.randint(1, n_tasks)
            tasks[index].append(v)
            if v in tasks.keys():
                tasks[v].append(index)
            else:
                tasks[v] = [index]
        else:
            v = random.randint(1, n_tasks)
            while (v == index):
                v = random.randint(1, n_tasks)
            tasks[index] = [v]
            if v in tasks.keys():
                tasks[v].append(index)
            else:
                tasks[v] = [index]
    print(tasks)
    return tasks


def createinputs(n_tasks, max_exec_time):
    inputs = []
    for i in range(1, n_tasks + 1):
        inputs.append([i, random.randrange(5, max_exec_time, 5)])
    print(inputs)
    return inputs
