from multiprocessing import Process
import sorting_algs as sgs
import demonstration as demo
import time

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




array_size = 1000
interaction_count = 1

task1_list_x = [] #count of iterations
task1_list_y = [] #output timestamp

task2_list_x = [] #count of iterations
task2_list_y = [] #output timestamp

task3_list_x = [] #count of iterations
task3_list_y = [] #output timestamp


for i in range(0, 10):

    ori_list = demo.get_data_arr(array_size)

    if __name__ == '__main__':
        run_cpu_tasks_in_parallel([
            task1_list_y.append(task_1(ori_list)),
            task2_list_y.append(task_2(ori_list)),
            task3_list_y.append(task_3(ori_list))
        ])

    interaction_count +=1
    array_size += 1000    
    
    print(array_size)

print(f'\n{task1_list_y}\n{task2_list_y}\n{task3_list_y}')