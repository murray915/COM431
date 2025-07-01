import file_data as fd
import json
import point_of_interest as poi
import random as rd

import menu_tree as mt
import user_inputs as ui

def main():

    rootnode = mt.build_menu_tree()
    main_menu = mt.get_main_menu(rootnode)

    exit = True

    while exit:
        user_input = ui.display_options(main_menu, 'Main Menu','menu option')

        # if user input exit leave program
        if user_input.replace(' ', '_') == "Exit":
            exit = False
            
        else:
            # print and user input for sub menu selected
            user_input = rootnode.get_child_data(user_input)            
            user_input = ui.display_options(user_input, 'Sub Menu', 'menu option')
            
            # if user input 6, print menu options
            if user_input.replace(' ', '_') != 'Return':
                
                # call function
                func = getattr(ui, 'mn_func_' + str(user_input.replace(' ', '_')))       
                output = func(rootnode)




def test():

    for i in range(0, 5):
        name = 'Hello-'+str(i)
        var_type = "POI"
        desc = str(rd.randrange(0,2000))+str(rd.randrange(0,2000))+"-DESC-"+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))
        quest = []

        for i in range(1, rd.randrange(2 ,5)):            
            question = "quest:::"+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))            
            ans = "ans==="+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))

            quest.append([question,ans])

        star = fd.data_file()
        poi_id = star.get_next_id()

        one = poi.point_of_interest(poi_id, name, var_type, desc, quest)
        star.add_data(one)
        star.save_to_file()

    # Opening JSON fileW
    with open('test.json') as f:
        data = json.load(f)

        print(data['meta_data'])

        for i in data['data']:
            print(i)

main()
