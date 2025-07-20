import sorting_algs as algs
import user_inputs as ui

def search_algs_select(poi_hs_table: object, user_search_value: int | str, user_input_sub: str, ask_question: bool) -> str | object | None:
    """ input hashtable, user_search_value, user_input_sub and ask user question. Return poi name, poi object and user answer OR None if not found """

    #general params
    tabulate_data = []
    search_list = []
    object_list = []
    header_list = ['Point of Interest ID','Point of Interest','Point of Interest Type','Description']
    ans = 'default'
    count = 0

    # get repo of pois & sort
    list_obj = poi_hs_table.search_in_chunks('items')
    outlist_sorted = algs.sort_str_list(list_obj,"ASC",0)

    print(user_input_sub, user_search_value)

    # If search user input is ID only
    if user_input_sub == "Search by Point of Interest ID":

        for i in outlist_sorted:
            if str(i[1].poi_attribute('id')) == str(user_search_value):
                poi_name = i[0]
                poi_obj = i[1]

                tabulate_data.append(i[1].poi_attribute('all_exc_ques_loc'))

                #print tabulate output to screen
                print('') 
                ui.print_data_tabulate(header_list, tabulate_data)
                print('') 

                return poi_name, poi_obj, ans
        else:        
            print(f'\n\nPoint of Interest not found. Please check Point of interest exists\n')
            return None, None, None
    
    else:
        # user params
        case_sens, fuzzy_sear = user_search_params(user_input_sub)
    
        # search list for value
        search_list = [i[0] for i in outlist_sorted]

        # Search Algorithms determined by input factors
            # binary search only selected for non-duplications & no fuzzy search
            # hashtable search only selected for non-duplications & no fuzzy search & Case sensitiy on
            # linear search to handle all other, duplications, fuzzy and case insensitve/sensitive

        for i in search_list:
            if i == user_search_value or user_search_value in i:
                count +=1

        if count >= 2 or fuzzy_sear == True:
            search_output  = linear_search(search_list, user_search_value, case_sens, fuzzy_sear)

        elif count == 1 and case_sens == True and fuzzy_sear == False:
            search_output = poi_hs_table.get_value(user_search_value)
            
            if search_output:
                search_output = [search_list.index(search_output.poi_attribute('name'))]

        else:
            search_output = binary_search(search_list, user_search_value, case_sens)

        # if not found exit delete
        if search_output is None:
            print(f'\n\nPoint of Interest not found. Please check Point of interest exists\n')
            return None, None, None

        else:
            #output data to correct format to print
            for i, value in enumerate(outlist_sorted):        
                if i in search_output:
                    tabulate_data.append(value[1].poi_attribute('all_exc_ques_loc'))
                    object_list.append([value[1].poi_attribute('name'), value[1]])

            #print tabulate output to screen
            print('') 
            ui.print_data_tabulate(header_list, tabulate_data)
            print('') 

            # get option list name & desc
            option_list = [[i[1], i[3]] for i in tabulate_data]

            # user input on update option
            if len(tabulate_data) == 1:
                
                # ask user to select value & return val
                if ask_question:
                    input_check = True
                else:
                    input_check = False

                while input_check:
                    ans = input(f'\n Select point of interest : {option_list[0][0]}, {option_list[0][1]}? Yes/No: ')

                    if ans.lower() not in ['yes','no']:
                        print('Please input "Yes" or "No"')
                    else:
                        input_check = False

                poi_name = object_list[0][0]
                poi_obj = object_list[0][1]

            else:
                option_list.append(['Exit','Leave operation, back to main menu'])
                list_poi_index = int(ui.display_options(option_list, 'Select Point of Interest from List','point of interest',True)) -1
                
                if list_poi_index <= len(object_list):
                    poi_name = object_list[list_poi_index][0]
                    poi_obj = object_list[list_poi_index][1]

    return poi_name, poi_obj, ans


def user_search_params(user_input_sub: str) -> str:
    """ get user input params for search """
    input_check = True

    # user params
    while input_check:
        user_case_input = input('Is search to be case sensitive? (Yes / No) : ').lower()
        if user_case_input == 'yes':
            case_sens = True
            input_check = False

        elif user_case_input == 'no':
            case_sens = False
            input_check = False

        else:
            print('Please either input "yes", or "no"')

    if 'Fuzzy' in user_input_sub:
        fuzzy_sear = True
    else:
        fuzzy_sear = False
    
    return case_sens, fuzzy_sear

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

def binary_search(search_list: list, search_value: str, search_sensitvity = True) -> list | None:
    """ input list to search in, and value to search for. Output position if found else None returned """
    """ Case Sensitive = True as default, input False to remove sensitivity """
    output = []

    # general params
    start_pos = 0
    end_pos = len(search_list) -1

    # loop through midpoints recursively until found
    while start_pos <= end_pos:        
        mid_point = start_pos + (end_pos - start_pos) // 2

        # if case sensitity True
        if search_sensitvity:      
            if search_list[mid_point] == search_value:
                output.append(mid_point)
                return output

            elif search_value < search_list[mid_point]:
                end_pos = mid_point -1

            else:
                start_pos = mid_point +1

        # if case sensitity False
        else:
            value = str(search_list[mid_point])
            if value.lower() == search_value.lower():
                output.append(mid_point)
                return output
            
            elif search_value < search_list[mid_point]:
                end_pos = mid_point -1

            else:
                start_pos = mid_point +1

    return None