import file_data as fd
import point_of_interest as poi
import demonstration as demo
import sorting_algs as algs
import searching_algs as sralgs
import queue_class as qc
import demonstration as demo

import os
from tabulate import tabulate


def display_options(all_options: list, title:str, type: str, return_opt = False) -> str | bool:
    """
    query_rows: must consist of a list of lists (two values) - id and description i.e. the category_id and category_description.
    title: is some text to put above the list of options to act as a title.
    type: is used to customise the prompt to make it appropriate for what you want the user to select.
    return_opt: if False, selected_option returned. If true, option number returned. Default FALSE 
    """
    try:
        option_num = 1
        option_list = []

        print("\n",title,"\n")        

        for option in all_options:
            code = option[0]
            desc = option[1]

            print("{0}.\t{1}".format(option_num, code))
            
            option_num = option_num + 1
            option_list.append(code)

        selected_option = 0

        while selected_option > len(option_list) or selected_option == 0:
            prompt = input("\nEnter the number against the "+type+" you want to choose: ")
            
            if not prompt.isnumeric():
                print(f'\n* ERROR * : Please enter only numbers (int)')
                selected_option = 0

            elif int(prompt) > len(option_list):
                print(f'\n* ERROR * : Please enter a number within the list')
                selected_option = 0
                
            else:
                selected_option = int(prompt)
        
        # returned value on return_opt
        if return_opt:
            return prompt
        else:
            return option_list[selected_option - 1]
    
    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} ** \n\n")
        return False
    

def print_data_tabulate(headers: list, data: list) -> None:
    """
    headers: str(s) within list
    data: raw data as list
    """   

    print(tabulate(
        data, 
        headers=headers
        ))
    

def mn_func_Add_Point_of_Interest(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ from user option to view menu descriptions; add POI or random POI records """
    
    # add POI via user input
    if user_input_sub == "Add point of Interest":
        # Option Data
        poi_types = [
            ["Restaurants",''],
            ["Museums",''],
            ["Parks",''],
            ["Hotels",''],
            ["Shopping Centers",''],
            ["Theaters",''],
            ["Historical Sites",''],
            ["Stadiums",''],
            ["Zoos",''],
            ["Other",'']
        ]   

        # User questions
        poi_id = poi_hs_table.get_next_index()
        name = input('Please input the name of the new Point of Interest: ')
        poi_type = display_options(poi_types, 'Point of Interest Types', 'Point of Interest type option')
        desc = input('Please input a description of the new Point of Interest: ')
        quest = []
        location  = input('Please input the location (contry) of the new Point of Interest: ')
        long_var = input('Please input the longitude of the new Point of Interest: ')
        lang_var = input('Please input the lonlatitude of the new Point of Interest: ')
        long_and_lang = [long_var, lang_var]

        poi_hs_table.put(name, poi.point_of_interest(poi_id, name, poi_type, desc, quest, location, long_and_lang))
    
    # add POI via random data input
    elif "Add random data point of Interest data" == user_input_sub:
        user_input = True

        while user_input:
            num_pois = input('Please input the number of random POI records to be created : ')       

            if num_pois.isnumeric() or num_pois.lower() == 'exit':
                user_input = False
                demo.create_test_pois(poi_hs_table, int(num_pois))
            else:
                print('Please input number values; or to exit this function, type "exit"')

    return poi_hs_table
    

def mn_func_Search_for_Point_of_Interests(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ from user option to view menu descriptions """
    #general params
    tabulate_data = []
    header_list = ['Point of Interest ID','Point of Interest','Point of Interest Type','Description']

    # user params
    if user_input_sub == "Search by Point of Interest ID":
        user_input = input('Please input the POI ID for the Point of Interest to get data for : ').strip()
    else:
        user_input = input('Please input the name of the Point of Interest to get data for : ').strip()

    poi_name, poi_obj, ans = sralgs.search_algs_select(poi_hs_table, user_input, user_input_sub, False)
    
    return poi_hs_table


def mn_func_Display_all_Points_of_Interest(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ display all points of interest within curr hashtable """

    # general params
    list_obj = poi_hs_table.search_in_chunks('values')
    header_list = ['Point of Interest ID','Point of Interest','Point of Interest Type','Description']
    tabulate_data = []
    sort_list = []
    data_list = []    
    sort_order = 'ASC'
    
    # get data list from hashtable
    for i in list_obj:
        sort_list.append(i.poi_attribute('name'))
        data_list.append([i.poi_attribute('name'), i.poi_attribute('all_exc_ques_loc')])

    # choose sorting alg; based on list size
    if poi_hs_table.__len__() < 300:
        sorted_list = algs.bubble_sort(sort_list)
    elif poi_hs_table.__len__() >= 300 and  poi_hs_table.__len__() < 1500:
        sorted_list = algs.merge_sort(sort_list)
    else:
        sorted_list = algs.quicksort(sort_list, 0, len(sort_list) -1)

    # sort data ASC/DESC
    if user_input_sub == "Display POIs by descending order":
        sorted_list.reverse()

    # output data to correct format to print
    for i in sorted_list:
        for j in data_list:
            if j[0] == i:
                tabulate_data.append(j[1])
                data_list.remove(j)

    # print tabulate output to screen
    print('')    
    print_data_tabulate(header_list, tabulate_data)
    print('')
    
    return poi_hs_table

def mn_func_Delete_Point_of_Interest(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ delete point of interest from user input """
    
    ans = 'default'
    user_search_value = input('Please input the name of the Point of Interest to get data for : ')
    poi_name, poi_obj, ans = sralgs.search_algs_select(poi_hs_table, user_search_value, user_input_sub, True)
    
    # user input, delete poi?
    if poi_name != None:
        if ans.lower() != 'no' and poi_name != 'Exit':
            poi_hs_table.remove_key(poi_name,poi_obj)

    print(f'\n\nPoint of Interest {poi_name} has been removed.')

    return poi_hs_table


def mn_func_Save_and_Load_Points_of_Interest_from_file(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ from user option to save & load files """

    # General params
    active_file = fd.data_file() # save file object
    dirname = os.path.dirname(__file__) # get current path
    filepath = dirname+'/data/' # default_path

    if user_input_sub == "Save to automatic location":
        
        # get filename
        filename = input('Please input what the save file name should be (file extention is added automatically): ')
        filepath = filepath+filename+'.json'

        try:
            # save file
            active_file.save_to_file(poi_hs_table, filepath)

        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n\tIf attempting to save a file, ensure that the filepath is input in full and correctly. \n\tCheck input, ensure they are forward slashed, and not within quotes or apostrophe example ; "
                  f"C:/Users/Murray/OneDrive/Documents/Uni/Playground/ \n\tUser input value was :: {filepath}")
            return False
    
    elif user_input_sub == "Save to user input location":
        
        # get filename & path
        filename = input('Please input what the save file name should be (file extention is added automatically): ')
        filepath = input('Please input the folderpath for the save file to be saved to (expected input format : "S:/Users/EMurray/OneDrive/Documents/Uni") : ')
        filepath = filepath+"/"+filename+'.json'
        
        try:
            # save file
            active_file.save_to_file(poi_hs_table, filepath)

        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n\tIf attempting to save a file, ensure that the filepath is input in full and correctly. \n\tCheck input, ensure they are forward slashed, and not within quotes or apostrophe example ; "
                  f"C:/Users/Murray/OneDrive/Documents/Uni/Playground/ \n\tUser input value was :: {filepath}")
            return False
    
    elif user_input_sub == "Load data from existing file - user selection":
        
        # get filename & path
        filepath = input('Please input the folderpath for the file to be loaded from to (expected input format : "S:/Users/EMurray/OneDrive/Documents/Uni") : ')

        # load file if exists        
        try:
            filepath = filepath+"/"+filename+'.json'
            output_list = active_file.load_data_from_file(filepath)
            
            for i in output_list:
                print(i.poi_attribute('name'))
                poi_hs_table.put(i.poi_attribute('name'),i)

        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n\tIf attempting to load a file, ensure that the filepath is input in full and correctly. \n\tCheck input, ensure they are forward slashed, and not within quotes or apostrophe example ; "
                  f"C:/Users/Murray/OneDrive/Documents/Uni/Playground/tester.json \n\tUser input value was :: {filepath}")
            return False
        
        
    elif user_input_sub == "Load data from existing file - example dev data":        
        
        # ask user for dataset size
        ans = display_options(
           [['Small Data Set',''],['Large Data Set',''],['Massive Data Set','']], 'Main Menu','menu option'
        )

        # load file
        if ans == "Small Data Set":
            output_list = active_file.load_data_from_file(filepath+"small_data_set.json")
        elif ans == "Large Data Set":
            output_list = active_file.load_data_from_file(filepath+"large_data_set.json")
        elif ans == "Massive Data Set":
            output_list = active_file.load_data_from_file(filepath+"mass_data_set.json")

        for i in output_list:
            print(i.poi_attribute('name'))
            poi_hs_table.put(i.poi_attribute('name'),i)


    elif user_input_sub == "View json file structure":

        # print json struc. from user input path
        try:

            filepath = input('Please input the full filepath for the file to be printed (expected input format : C:/Users/Murray/OneDrive/Documents/Uni/jsontester.json") : ')
            active_file.view_json_file(filepath)

        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n\tIf attempting to load a file, ensure that the filepath is input in full and correctly. \n\tCheck input, ensure they are forward slashed, and not within quotes or apostrophe example ; "
                  f"C:/Users/Murray/OneDrive/Documents/Uni/Playground/tester.json \n\tUser input value was :: {filepath}")
            return False
        
    return poi_hs_table


def mn_func_Questions_and_Answers_for_Points_of_Interest(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ from user option to update poi with questions/answers """
    ans = 'default'
    user_search_value = input('Please input the name of the Point of Interest to get data for : ')
    # Default to fuzzy search
    poi_name, poi_obj, ans = sralgs.search_algs_select(poi_hs_table, user_search_value, "Fuzzy",True)
        
    # user input, update poi?
    if poi_name != None:
        if ans.lower() != 'no' and poi_name != 'Exit':
            header_list = ['Questions','Answers']
            question_data = []

            quest_ans = poi_obj.poi_attribute('quest')

            if not quest_ans and user_input_sub == 'Add answer to Point of Interest':
                print('There are no questions to answer for this point of interest')

            else:
                quest_que = qc.Queue(12)

                for i in quest_ans:
                    quest_que.enqueue(i)
                    question_data.append((i[0],i[1]))
                
                #print tabulate output to screen
                print(f'\nCurrent Questions for Point of Interest.\n\nThese are answered in top to bottom order, and once answered are removed\n')
                print_data_tabulate(header_list, question_data)
                print('')

                if user_input_sub == "Add answer to Point of Interest":
                    input(f'\nPlease input an answer to the next question :: \n{quest_que.get_next_value()[0]}\n:')
                    quest_que.dequeue()
                else:
                    quest_que.enqueue([input(f'\nPlease input a question to add to the point of interest : '),''])

                question_data = []

                while quest_que.get_next_value() != False:
                    question_data.append(quest_que.get_next_value())
                    quest_que.dequeue()
                                
                poi_obj.user_ques_ans_update(question_data)

    return poi_hs_table

def mn_func_View_Menu_option_descriptions(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ from user option to view menu descriptions """
    
    # get main menu
    outputlist = []
    for i in range(0, len(treenode.children)):
        outputlist.append([treenode.children[i].data, treenode.children[i].desc])

    headers = ["Option","Description"]
    
    print('')
    print_data_tabulate(headers, outputlist)                        
    print('')

    return poi_hs_table

def mn_func_Demonstration_of_Data_Structures_and_Algorithms(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ from user option to view menu descriptions """

    sublist = treenode.get_child_data("Demonstration of Data Structures and Algorithms",user_input_sub)
    
    # request sub menu option
    demo_sub = display_options(sublist, 'Sub Menu Runset Options', 'menu option')

    #call submenu (where not Return / exit)
    if demo_sub.replace(' ', '_') == 'Return':
        return poi_hs_table

    elif 'sort' not in demo_sub.lower():
        print(f'data {demo_sub}')

        # call function
        getattr(demo, 'demo_' + str(demo_sub.replace(' ', '_').lower()))()
    
    elif 'sort' in demo_sub.lower():
        print(f'sort {demo_sub}')

        #params
        print_cons = True        
        check = True

        while check:
            user_input = input('Please input number of example data to sort (greater than or equal to 11) : ')
            
            if user_input.isnumeric():
                if int(user_input) >= 11:
                    example_size = int(user_input)        
                    check = False

        ori_list = demo.get_data_arr(example_size)
        runset = str(demo_sub.replace(' ', '_').lower())

        # call function
        demo.demo_sorting_algr(ori_list, print_cons, runset)


    return poi_hs_table