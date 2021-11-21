import configparser

reader = configparser.ConfigParser()
reader.read(r"C:\Users\saiak\PycharmProjects\VimanTest\config.ini")
param = reader["Scheduling Parameters"]


def HeristicBinPacking(tasks, conflict_graph):
    print("STARTING THE HEURISTIC BIN PACKING !!!!!!!")
    task_sort = sorted(tasks, key=lambda x: x[1], reverse=True)
    task_sort_dum = sorted(tasks, key=lambda x: x[1], reverse=True)
    time_here = 0
    b_c = 0
    mla = int(param["mla"])
    bin_size = int(param["bin_size"])
    rec = {}
    exec_order = []
    while (len(rec) < len(tasks)):
        l_key = []
        l_val = []
        b_c += 1
        task_sort = sorted(task_sort_dum, key=lambda x: x[1], reverse=True)
        for i in task_sort:
            if i[0] in rec.keys():
                continue
            c = 0
            if len(l_key) >= mla:
                break
            if len(l_key) == 0:
                l_key.append(i[0])
                # print("Updated l_key : {}".format(l_key))
                if i[1] <= bin_size:
                    rec[i[0]] = True
                    task_sort_dum.remove(i)
                    time_here += i[1]
                else:
                    task_sort_dum.remove(i)
                    i[1] -= bin_size
                    time_here += bin_size
                    task_sort_dum.append(i)
                print("Task " + str(i[0]) + " is inserted into the " + str(b_c) + "th bin as bin is empty")
                if i[0] in conflict_graph.keys():
                    for j in conflict_graph[i[0]]:
                        l_val.append(j)
                # print("Updated l_val : {}".format(l_val))
                continue
            if i[0] in l_val:
                continue
            if i[0] in conflict_graph.keys():
                for k in l_key:
                    if k in conflict_graph[i[0]]:
                        c += 1
                        break
            if c != 0:
                continue
            l_key.append(i[0])
            if i[1] <= bin_size:
                rec[i[0]] = True
                task_sort_dum.remove(i)
            else:
                task_sort_dum.remove(i)
                i[1] -= bin_size
                task_sort_dum.append(i)
            print("Task " + str(i[0]) + " is inserted into the " + str(b_c) + "th bin")
            if i[0] in conflict_graph.keys():
                for j in conflict_graph[i[0]]:
                    l_val.append(j)
            # print("Updated l_val : {}".format(l_val))
        print("Tasks in this bin are: {} ".format(l_key))
        exec_order.append(l_key)
        print("All the tasks till " + str(b_c) + "th bin will be executed within " + str(time_here) + " seconds")
    print("Execution order of tasks is {}".format(exec_order))
    print(
        "OVERALL ALL THE TASKS WILL BE EXECUTED IN cycle time of " + str(time_here) + " SECONDS WITH USAGE OF " + str(b_c) + " BINS")
    return
