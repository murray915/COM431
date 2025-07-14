import file_data as fd
import stack_class as sc
import hashtable as hs
import point_of_interest as poi
import demonstration as demo
import sorting_algs as algs
import searching_algs as sralgs

import os
from tabulate import tabulate



def display_options(all_options: list, title:str, type: str) -> str | bool:
    """
    query_rows: must consist of a list of lists (two values) - id and description i.e. the category_id and category_description.
    title: is some text to put above the list of options to act as a title.
    type: is used to customise the prompt to make it appropriate for what you want the user to select.
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
        headers=headers,
        numalign="right",
        stralign="center",
        colalign=("left", "left", "left")
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

        poi_hs_table.put(name, poi.point_of_interest(poi_id, name, poi_type, desc, quest))
    
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
    search_list = []
    header_list = ['Point of Interest ID','Point of Interest','Point of Interest Type','Description']
    
    # get data list from hashtable
    list_obj = poi_hs_table.search_in_chunks('values')
    outlist_sorted = algs.sort_str_list(list_obj,"ASC",0)

    # user params
    if input('Is search to be case sensitive? (Yes / No) : ').lower() == 'yes':
        case_sens = True
    else:
        case_sens = False

    user_input = input('Please input the name of the Point of Interest to get data for : ')

    if user_input_sub in ["Manual input search - Fuzzy","Letter search for POI(s)"]:
        fuzzy_sear = True
    else:
        fuzzy_sear = False

    # search list for value
    search_list = [i[0] for i in outlist_sorted]
    search_output = sralgs.search_algs_select(search_list, case_sens, fuzzy_sear, user_input)
    

    # output data to correct format to print
    for i in search_output:
        tabulate_data.append(data_list[i][0])

    # print tabulate output to screen
    print('')    
    print_data_tabulate(header_list, tabulate_data)
    print('')

    return poi_hs_table

def mn_func_View_Menu_option_descriptions(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ from user option to view menu descriptions """
    
    # get main menu
    outputlist = []
    for i in range(0, len(treenode.children)):
        outputlist.append([treenode.children[i].data, treenode.children[i].desc])

    headers = ["Option","Description"]
    
    print('')
    print_data_tabulate(headers, 
                        outputlist)                        
    print('')

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
        data_list.append([i.poi_attribute('name'), i.poi_attribute('all')])

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



if __name__ == '__main__':
    pass