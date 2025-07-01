from tabulate import tabulate

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
    

def mn_func_View_Menu_Descriptions(treenode: object):
    """ from user option to view menu descriptions """
    
    # get main menu
    outputlist = []
    for i in range(0, len(treenode.children)):
        outputlist.append([treenode.children[i].data, treenode.children[i].desc])

    headers = ["Option","Description"]
    
    print('')
    print_data_tabulate(headers, outputlist)
    print('')

