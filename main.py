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


main()




# if __name__ == '__main__':
#     import os
#     import searching_algs as seralg

#     treenode = ''
#     poi_hs_table = hs.Hashmap(100)
#     actfile = fd.data_file()

#     # get test data
#     poi_hs_table = demo.create_test_pois(poi_hs_table, 20)

#     # get paths
#     dirname = os.path.dirname(__file__)
#     filepath = dirname+'/data/'

#     user_input_sub = "Add question to Point of Interest"
    
#     ui.mn_func_Questions_and_Answers_for_Points_of_Interest(treenode, poi_hs_table, user_input_sub)