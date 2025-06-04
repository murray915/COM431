
# Key notes / learning sources 
    # - https://realpython.com/sorting-algorithms-python/
    # - https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php
    # - https://stackabuse.com/bubble-sort-in-python/
    # - https://www.youtube.com/watch?v=cVZMah9kEjI 
    # - https://www.datacamp.com/tutorial/python-merge-sort-tutorial


def bubble_sort(arr) -> bool:
    """ bubble sort algorithm: added opt to exit loop after swap """
    try:
        action_taken = True

        # set actiontaken as False until swap
        while(action_taken):
            action_taken = False

            # start at the end of list, until start
            for num in range(len(arr)-1,0,-1):

                # cycle through list move value 
                # if larger to right within list
                for i in range(num):
                    if arr[i]>arr[i+1]:
                        # alt code = arr[i], arr[i+1] = arr[i+1], arr[i]
                        temp = arr[i]
                        arr[i] = arr[i+1]
                        arr[i+1] = temp

                        action_taken = True
        return True
    
    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
        return False


def merge_sort(list_arr: list):
    """ merge sort, input left/right arrays """
    if len(list_arr) > 1:
        # get midpoint
        midpoint = len(list_arr)//2
        left_half = list_arr[:midpoint]
        right_half = list_arr[midpoint:]
        
        # recusion point
        merge_sort(left_half)
        merge_sort(right_half)

        # set count vars
        i = j = k = 0

        # check front value of lists, add smaller int
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_arr[k] = left_half[i]                
                i += 1
            else:
                list_arr[k] = right_half[j]
                j += 1
            k += 1
        
        # add remaining values into list
        while i < len(left_half):
            list_arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list_arr[k] = right_half[j]
            j += 1
            k += 1



import random as rd
import time

def test_arlg_timing(ori_list):
    start_time = time.time()

    merge_sort(ori_list)
    print(f'Output value list: \n {ori_list}')
    print("--- Run completed in %s seconds ---" % (time.time() - start_time))


runset = 'merge_sort'
ori_list = []
for _ in range(0, rd.randrange(10,70)):
    ori_list.append(rd.randrange(0,10000))

print(f'Length of list: {len(ori_list)}, action on runset {runset}:\nOriginal list: \n {ori_list}')
test_arlg_timing(ori_list)