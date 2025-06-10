import random as rd
import time
import sorting_algs as algs

def test_arlg_timing(ori_list, print_cons, runset):
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



runset = 'bubble_sort'
print_cons = True

ori_list = []
for _ in range(0, rd.randrange(10,15)):
    ori_list.append(rd.randrange(0,10000))

test_arlg_timing(ori_list, print_cons, runset)