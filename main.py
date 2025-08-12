import graphics as ghp
import menu_tree as mt
import user_inputs as ui
import hashtable as hs


def main():

    ghp.welcome_screen()
    rootnode = mt.build_menu_tree()
    main_menu = mt.get_main_menu(rootnode)

    exit = True
    poi_hs_table = hs.Hashmap(127)

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

    ghp.exit_screen()


main()