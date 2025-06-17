import random as rd
import time
import sorting_algs as algs
import queue_class as qc
import stack_class as sc

def get_data_arr(top_range = 15) -> list:
    """ return large random array ; input top random size """
    ori_list = []
    for _ in range(0, rd.randrange(10,top_range)):
        ori_list.append(rd.randrange(0,10000))

    return ori_list


def demo_sorting_algr(ori_list, print_cons, runset):
    """ demo sorting algr ; input sorting algr name """
    start_time = time.time()

    if print_cons:
        print("-----------------------------------------------------------------")
        print(f'Length of list: {len(ori_list)}, action on runset {runset}:\nOriginal list: \n {ori_list}')
        print(f"-----------------------------------------------------------------\n\n")

    try:
        # set runset as varible function
        func = getattr(algs, runset)

        # Call runset
        if "quicksort" in runset:
            func(ori_list, 0, len(ori_list) -1, print_cons)
        else:
            func(ori_list, print_cons)
            
    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")

    if print_cons:
        print(f'----------------------------------------------------------------- \nFinal Output value list: \n {ori_list}')
        print("  --- Run completed in %s seconds ---" % (time.time() - start_time))
        print("-----------------------------------------------------------------")

def demo_stack_data_type():
    """ demo sorting algr ; input sorting algr name """
    demo_stack = sc.Stack()

    print(f'Demo for Stack, random add / remove actions and results')

    for _ in range(1, rd.randrange(2,8)):
        num = rd.randrange(1,8)        
        print(f'\tadd to stack {num}')
        demo_stack.stack_add(num)

    for _ in range(1, rd.randrange(2,5)):      
        print(f'\tremove from stack')
        demo_stack.stack_remove()

    demo_stack.print_queue()
    

def demo_queue_data_type():
    """ demo sorting algr ; input sorting algr name """
    demo_que = qc.Queue(8)

    print(f'Demo for queue, random enqueue / dequeue actions and results')

    for _ in range(1, rd.randrange(2,8)):
        num = rd.randrange(1,8)        
        print(f'\tadd to queue {num}')
        demo_que.enqueue(num)

    for _ in range(1, rd.randrange(2,5)):      
        print(f'\tdequeue')
        demo_que.dequeue()

    demo_que.print_queue()
    



runset = 'bubble_sort'
print_cons = True
ori_list = get_data_arr()

demo_sorting_algr(ori_list, print_cons, runset)
demo_queue_data_type()
demo_stack_data_type()
