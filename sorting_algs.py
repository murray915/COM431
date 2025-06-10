# Key notes / learning sources 
    # - https://realpython.com/sorting-algorithms-python/
    # - https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php
    # - https://stackabuse.com/bubble-sort-in-python/
    # - https://www.youtube.com/watch?v=cVZMah9kEjI 
    # - https://www.datacamp.com/tutorial/python-merge-sort-tutorial


def bubble_sort(arr, print_cons = False) -> bool:
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


def merge_sort(list_arr: list, print_cons = False):
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


def quicksort(arr: list, left: int, right:int, print_cons = False):
    """ quicksort, input left/right arrays """
    if left < right:
        # get first partition for recursion
        partition_pos = partition(arr, left, right, print_cons)

        # split arr left/right recursion to end sort
        quicksort(arr, left, partition_pos -1, print_cons)
        quicksort(arr, partition_pos +1, right, print_cons)


def partition(arr: list, left: int, right: int, print_cons: bool):
    """ action input arr left/ right against pivot value"""
    # set start points
    i = left
    j = right - 1
    pivot = arr[right]

    # move through list
    # i = ASC, j = DESC
    while i < j:
        if print_cons:
            print(f'\nBegining point, \nleft: {left}, right: {right-1}, pivot: {pivot} \n{arr}')

        while i < right and arr[i] < pivot:
            if print_cons:
                print(f'i value: {arr[i]}, index {i}')
            i +=1

        if print_cons:
            print(f'final i {arr[i]}, index {i}')

        while j > left and arr[j] >= pivot:
            if print_cons:
                print(f'j value: {arr[j]}, index {j}')
            j -=1
        
        if print_cons:
            print(f'final j {arr[j]}, index {j}')

        # at endpoint of search
        # switch i & j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            if print_cons:
                print(f'swap i & j: \ni value at index {i} less than pivot - {arr[i]} \nj value at index {j} greater than pivot - {arr[j]} \n Output point \n{arr}\n\n')

    # endpoint found switch values
    if arr[i] > pivot:
        if print_cons:
            print(f'\nj is no longer greater than i, {j} / {i} \nBegining point, \nleft: {left}, right: {right-1}, pivot: {pivot} \n{arr}')
        arr[i], arr[right] = arr[right], arr[i]

        if print_cons:
            print(f'swap end point : {arr[i]}, {arr[right]}')    
    
    # return new partition point for recursion
    return i