
def lexicographically_compare_two_strs(str_1: str, str_2: str, orderby = "ASC") -> list:    
    """ input two strings, output correct order of strings in list """
    
    for x, y in zip(str_1, str_2):
        
        if x == y: # if same continue
            continue
        elif x > y: # if x larger, return list
            
            if orderby == "DESC":
                return [str_2,str_1]
            else:
                return [str_1,str_2]
            
    else:  # if x not greater than y, return list as is
        
        if orderby == "DESC":
            # check and return longer str last
            if len(str_1) > len(str_2):
                return [str_1,str_2]
            else:
                return [str_2,str_1]
        else:
            # check and return longer str last
            if len(str_1) > len(str_2):
                return [str_2,str_1]
            else:
                return [str_1,str_2]


def bubble_sort(arr, print_cons = False) -> list | bool:
    """ bubble sort algorithm: added opt to exit loop after swap """
    try:
        action_taken = True

        if print_cons:
            print(f'Begining point, \n{arr}\n\n')

        # set actiontaken as False until swap
        while(action_taken):
            action_taken = False

            # start at the end of list, until start
            for num in range(len(arr)-1,0,-1):

                # cycle through list move value 
                # if larger to right within list
                for i in range(num):
                    if arr[i]>arr[i+1]:
                        if print_cons:
                            print(f'Before change: \n\t{arr}')
                            print(f'Update: \n\t{arr[i]} > {arr[i+1]}, switch values in array')

                        # alt code = arr[i], arr[i+1] = arr[i+1], arr[i]
                        temp = arr[i]
                        arr[i] = arr[i+1]
                        arr[i+1] = temp

                        if print_cons:
                            print(f'After change: \n\t{arr}\n')
                        action_taken = True

        return arr
    
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
        merge_sort(left_half, print_cons)
        merge_sort(right_half, print_cons)

        if print_cons:
            print(f'\nMidpoint place choosen : {midpoint}')
            print(f'\t Left arr : {left_half}')
            print(f'\t Right arr : {right_half}')

        # set count vars
        i = j = k = 0

        # check front value of lists, add smaller int
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_arr[k] = left_half[i]  

                if print_cons:
                    print(f'\t Add to new arr : {list_arr[k]} from left half as it is smaller than right : {left_half[i]} / {right_half[j]}')
                
                i += 1

            else:
                list_arr[k] = right_half[j]
                
                if print_cons:
                    print(f'\t Add to new arr : {list_arr[k]} from right half as it is smaller than left : {right_half[j]} / {left_half[i]}')
                
                j += 1
            k += 1
        

        # add remaining values into list
        while i < len(left_half):
            list_arr[k] = left_half[i]

            if print_cons:
                print(f'\t Add remaining list to arr : {list_arr[k]} from left half')
                  
            i += 1
            k += 1

        while j < len(right_half):
            list_arr[k] = right_half[j]

            if print_cons:
                print(f'\t Add remaining list to arr : {list_arr[k]} from right half')

            j += 1
            k += 1

    return list_arr

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


def sort_str_list(str_list: list, orderby = "ASC", list_index_sort = 0) -> list | bool:
    """ sort list of strings (or list of lists/tuples) return ASC list. If not list/tuple/int/str or error on sort False returned """
    
    try:
           
        if isinstance(str_list[0], (list, tuple)):

            # correct formatting to str of str(s)
            output_list=[]

            # remove min/max respective of orderby
            # found value into new output list
            while str_list:
                if orderby == "ASC":
                    res = min(str(i[list_index_sort]) for i in str_list)
                    for i, element in enumerate(str_list):
                        if element[list_index_sort] == res:
                            output_list.append(element)
                            str_list.pop(i)
                else:
                    res = max(str(i[list_index_sort]) for i in str_list)
                    for i, element in enumerate(str_list):
                        if element[list_index_sort] == res:
                            output_list.append(element)
                            str_list.pop(i)

        elif isinstance(str_list[0], (int, str)):

            if isinstance(str_list[0], str):

                # correct formatting to str of str(s)                
                output_str  = ",".join(str_list)
                l=output_str.split(',')
                output_list=[]

                # remove min/max respective of orderby
                # found value into new output list
                while l:
                    if orderby == "ASC":
                        output_list+=[l.pop(l.index(min(l)))]
                    else:
                        output_list+=[l.pop(l.index(max(l)))]

            else:
                l = str_list.copy()
                output_list=[]

                # remove min/max respective of orderby
                # found value into new output list
                while l:
                        if orderby.upper() == "ASC":
                            output_list.append(l.pop(l.index(min(l))))
                        else:
                            output_list.append(l.pop(l.index(max(l))))
           
        else:
            return False
        

    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} ** \n\n")
        return False
    
    return output_list