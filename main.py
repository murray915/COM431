import file_data as fd
import json
import point_of_interest as poi
import random as rd
import demonstration as demo
import sorting_algs as algs
import searching_algs as sralgs

import menu_tree as mt
import user_inputs as ui
import hashtable as hs
from tabulate import tabulate

def main():

    rootnode = mt.build_menu_tree()
    main_menu = mt.get_main_menu(rootnode)

    exit = True
    poi_hs_table = hs.Hashmap(100)

    # get test data
    poi_hs_table = demo.create_test_pois(poi_hs_table, 150)

    while exit:
        user_input_main = ui.display_options(main_menu, 'Main Menu','menu option')

        # if user input exit leave program
        if user_input_main.replace(' ', '_') == "Exit":
            exit = False
            
        else:
            # print and user input for sub menu selected
            user_input_sub = rootnode.get_child_data(user_input_main)            
            user_input_sub = ui.display_options(user_input_sub, 'Sub Menu', 'menu option')
            
            # if user input 6, print menu options
            if user_input_sub.replace(' ', '_') != 'Return':
                
                # call function
                func = getattr(ui, 'mn_func_' + str(user_input_main.replace(' ', '_')))       
                poi_hs_table = func(rootnode, poi_hs_table, user_input_sub)  


#main()


if __name__ == '__main__':
    import os

    treenode = ''
    poi_hs_table = hs.Hashmap(100)
    actfile = fd.data_file()

    # get test data
    poi_hs_table = demo.create_test_pois(poi_hs_table, 20 )

    # get paths
    dirname = os.path.dirname(__file__)
    filepath = dirname+'/data/'
    
    user_input_sub = 'Manual input search - Fuzzy'


    #general params
    tabulate_data = []
    search_list = []
    header_list = ['Point of Interest ID','Point of Interest','Point of Interest Type','Description']

    #ui.mn_func_Search_for_Point_of_Interests(treenode, poi_hs_table, user_input)
    list_obj = poi_hs_table.search_in_chunks('items')

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
    
    print(f'\n\n{search_output}\n\n')


    #output data to correct format to print
    for i, value in enumerate(outlist_sorted):
        if i in search_output:
            tabulate_data.append(value[1].poi_attribute('all'))

    # print tabulate output to screen
    print('')    
    ui.print_data_tabulate(header_list, tabulate_data)
    print('')

    


