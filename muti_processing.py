from multiprocessing import Process, freeze_support, set_start_method

import matplotlib.pyplot as plt
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

    return round((time.time() - start_time),5)

def task_2(ori_list: list):
    start_time = time.time()
    output = sgs.merge_sort(ori_list)

    return round((time.time() - start_time),5)

def task_3(ori_list: list):
    start_time = time.time()
    output = sgs.quicksort(ori_list, 0, len(ori_list) -1)

    return round((time.time() - start_time),5)

def task_4(ori_list: list):
    start_time = time.time()
    output = sgs.sort_str_list(ori_list)

    return round((time.time() - start_time),5)
    
def run_alg_tester():
    out1 = []
    out2 = []
    out3 = []
    out4 = []
    x = []

    data_size = 1000
    ori_list = demo.get_data_arr(data_size)

    sys.setrecursionlimit(10_000)

    for i in range(0,10):

        run_cpu_tasks_in_parallel([
                out1.append(task_1(ori_list)),
                out2.append(task_2(ori_list)),
                out3.append(task_3(ori_list)),
                out4.append(task_4(ori_list))
            ])

        x.append(data_size)

        data_size += 250
        ori_list.extend(demo.get_data_arr(data_size))

    bubble_sort = out1
    merge_sort = out2
    quick_sort = out3
    min_max_sort = out4

    plt.plot(x, bubble_sort, label ='Bubble Sort')
    plt.plot(x, merge_sort, '-.', label ='Merge Sort')
    plt.plot(x, quick_sort, '-', label ='Quick Sort')
    plt.plot(x, min_max_sort, '-', label ='MIN/MAX Sort')

    plt.xlabel("Number of Data points")
    plt.ylabel("Number of Seconds")
    plt.legend()
    plt.title('Sorting Algorithms Time Test')
    plt.show()



def run_sorting_test():
    freeze_support()
    set_start_method('spawn')
    p = Process(target=run_alg_tester)
    p.start()



if __name__ == '__main__':
    run_sorting_test()