from multiprocessing import Process
import sorting_algs as sgs
import demonstration as demo
import time
import sys

def run_cpu_tasks_in_parallel(tasks):
    running_tasks = [Process(target=task) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()

def task_1(ori_list: list):
    start_time = time.time()
    output = sgs.bubble_sort(ori_list)

    #print("--- Bubble sort completed :: %s seconds ---" % (time.time() - start_time))

    return round((time.time() - start_time),5)

def task_2(ori_list: list):
    start_time = time.time()
    output = sgs.merge_sort(ori_list)

    #print("--- Merge sort completed :: %s seconds ---" % (time.time() - start_time))

    return round((time.time() - start_time),5)

def task_3(ori_list: list):
    start_time = time.time()
    output = sgs.quicksort(ori_list, 0, len(ori_list) -1)

    #print("--- Quicksort sort completed :: %s seconds ---" % (time.time() - start_time))

    return round((time.time() - start_time),5)

out1 = []
out2 = []
out3 = []
x = []
y = []
data_size = 1000
ori_list = demo.get_data_arr(data_size)

if __name__ == '__main__':
    sys.setrecursionlimit(10_000)

    for i in range(0,10):

        run_cpu_tasks_in_parallel([
                out1.append(task_1(ori_list)),
                out2.append(task_2(ori_list)),
                out3.append(task_3(ori_list))
            ])

        x.append(data_size)

        data_size += 250
        ori_list.extend(demo.get_data_arr(data_size))

    #print(out1, out2, out3)


    # importing package
    import matplotlib.pyplot as plt

    bubble_sort = out1
    merge_sort = out2
    quick_sort = out3

    plt.plot(x, bubble_sort, label ='bubble_sort')
    plt.plot(x, merge_sort, '-.', label ='merge_sort')
    plt.plot(x, quick_sort, '-', label ='quick_sort')

    plt.xlabel("Number of Data points")
    plt.ylabel("Number of Seconds")
    plt.legend()
    plt.title('multiple plots')
    plt.show()
