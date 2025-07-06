
def search_algs_select(sorted_list: list, case_sens: bool, fuzzy_sear: bool, user_search_val: int | str) -> int | list | None:
    """ input list of selection options, return position of value or list of possible values """

    if sorted_list.count(user_search_val) >= 2 or case_sens == False or fuzzy_sear == True:
        return linear_search(sorted_list, user_search_val, case_sens, True)
    else:
        return binary_search(sorted_list, user_search_val, case_sens)
    

def linear_search(search_list: list, search_value: str, search_sensitvity = True, search_fuzzy = False) -> int | list | None | bool:
    """ input list to search in, and value to search for. Output position if found non fuzzy, if fuzzy list returns of all possible positions, else None returned """
    """ Case Sensitive = True as default, input False to remove sensitivity """
    """ Fuzzy search = False as default, input True to search for any positions which contain (case non-sensitive) the search value """

    if isinstance(search_value, int) and search_sensitvity == False:
        print('Search value has been passed as integer and search Case Insensitive. If list contains int(s), search without input False for sensitivity')        
        return None

    output_list = []
        
    try:
        for i in range(0, len(search_list)):

            # if fuzzy search is off
            if search_fuzzy == False:

                # if case sensitivity off
                if search_sensitvity == False and str(i).lower() == search_value.lower():
                    return i
                # if case sensitivity on
                elif search_sensitvity == True and i == search_value:
                    return i
            
            # if fuzzy search is on
            else:

                if search_sensitvity == False and search_value.lower() in str(search_list[i]).lower():
                    output_list.append(i)
                elif search_sensitvity == True and str(search_value) in str(search_list[i]):
                    output_list.append(i)
            
        if not output_list:
            return None
        else:
            return output_list      
         
    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
        return False

def binary_search(search_list: list, search_value: str, search_sensitvity = True) -> int | None:
    """ input list to search in, and value to search for. Output position if found else None returned """
    """ Case Sensitive = True as default, input False to remove sensitivity """

    if isinstance(search_value, int) and search_sensitvity == False:
        print('Search value has been passed as integer and search Case Insensitive. If list contains int(s), search without input False for sensitivity')        
        return None

    # general params
    start_pos = 0
    end_pos = len(search_list) -1

    # loop through midpoints recursively until found
    while start_pos <= end_pos:
        mid_point = start_pos + (end_pos - start_pos) // 2

        # if case sensitity True
        if search_sensitvity:            
            if search_sensitvity == True and search_list[mid_point] == search_value:
                return mid_point

            elif search_value < search_list[mid_point]:
                end_pos = mid_point -1

            else:
                start_pos = mid_point +1

        # if case sensitity False
        else:
            if search_sensitvity == False and (str(search_list[mid_point]).lower() == search_value.lower()):
                return mid_point
            
            elif search_value < search_list[mid_point]:
                end_pos = mid_point -1

            else:
                start_pos = mid_point +1

    return None