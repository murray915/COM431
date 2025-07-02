from tabulate import tabulate
import os
import file_data as fd

def display_options(all_options: list, title:str, type: str) -> str | bool:
    """
    query_rows: must consist of two values - id and description i.e. the category_id and category_description.
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
        headers=headers
        ))
    

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

         # save file
        active_file.save_to_file(poi_hs_table, filepath)

    elif user_input_sub == "Save to user input location":
        
        # get filename & path
        filename = input('Please input what the save file name should be (file extention is added automatically): ')
        filepath = input('Please input the folderpath for the save file to be saved to (expected input format : "S:/Users/EMurray/OneDrive/Documents/Uni") : ')
        filepath = filepath+"/"+filename+'.json'
        
         # save file
        active_file.save_to_file(poi_hs_table, filepath)

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
    
    print('\nfor testing\n')
    list_obj = poi_hs_table.search_in_chunks('values')

    for i in list_obj:
        print(i.poi_attribute('name'))
    
    return poi_hs_table