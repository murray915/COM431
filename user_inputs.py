import file_data as fd
import point_of_interest as poi
import demonstration as demo
import sorting_algs as algs
import searching_algs as sralgs
import queue_class as qc
import demonstration as demo
import routing as rout
import stack_class as sc
import muti_processing as multi
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

        stack = sc.Stack()

        # User questions
        stack.stack_add(poi_hs_table.get_next_index())
        stack.stack_add(input('Please input the name of the new Point of Interest: '))
        stack.stack_add(display_options(poi_types, 'Point of Interest Types', 'Point of Interest type option'))
        stack.stack_add(input('Please input a description of the new Point of Interest: '))        
        stack.stack_add([])        
        stack.stack_add(input('Please input the location (contry) of the new Point of Interest: '))

        long_var = input('Please input the longitude of the new Point of Interest: ')
        lang_var = input('Please input the lonlatitude of the new Point of Interest: ')
        stack.stack_add([long_var, lang_var])

        data = stack.stack_all_data()

        poi_hs_table.put(data[0], poi.point_of_interest(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    
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

    # user params
    if user_input_sub == "Search by Point of Interest ID":
        user_input = input('Please input the POI ID for the Point of Interest to get data for : ').strip()
    else:
        user_input = input('Please input the name of the Point of Interest to get data for : ').strip()
        
    poi_name, poi_obj, ans = sralgs.search_algs_select(poi_hs_table, user_input, user_input_sub, True)
    
    # user input, delete poi?
    if poi_name != None:
        if ans.lower() != 'no' and poi_name != 'Exit':
            poi_hs_table.remove_key(poi_name,poi_obj)

    if poi_name:
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
        filename = input('Please input what the save file name should be (file extention is added automatically): ').replace(' ', '_').lower()
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
        filename = input('Please input what the save file name should be (file extention is added automatically): ').replace(' ', '_').lower()
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
        fullpath = input('Please input the fullpath for the file to be loaded from to (expected input format : "S:/Users/EMurray/OneDrive/Documents/Uni/value.json") : ')

        # load file if exists        
        try:            
            filepath = fullpath
            output_list = active_file.load_data_from_file(filepath)
            
            for i in output_list:
                print(i.poi_attribute('name'))
                poi_hs_table.put(i.poi_attribute('name'),i)

            poi_hs_table.update_hashtable_poi_index()

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

        poi_hs_table.update_hashtable_poi_index()

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
    
    if user_input_sub == "View Menu Tree":
        treenode.print_tree()
    else:
        # get main menu
        outputlist = []
        for i in range(0, len(treenode.children)):
            outputlist.append([treenode.children[i].data, treenode.children[i].desc])

        headers = ["Option","Description"]
        
        print('')
        print_data_tabulate(headers, outputlist)                        
        print('')

    return poi_hs_table

def mn_func_Router_from_Point_of_Interest_to_Point_of_Interest(treenode: object, poi_hs_table: object, user_input_sub: str) -> object:
    """ from user option to view menu descriptions """

    point_of_interest_list = [
            ["Cardiff Castle", "A medieval castle and Victorian Gothic revival mansion in the city centre, with over 2,000 years of history."],
            ["Animal Wall", "A famous wall with sculpted animals, designed by architect William Burges in the 19th century."],
            ["St John the Baptist Church", "One of Cardiffs oldest churches, dating back to the 12th century, located near the city centre."],
            ["City Hall", "An Edwardian baroque-style civic building in Cathays Park, known for its grand architecture and public events."],
            ["Pierhead Building", "A historic red-brick building in Cardiff Bay, now a museum and visitor centre telling the story of Welsh politics."],
            ["St Davids Hall", "Cardiffs premier concert venue and home of the BBC Cardiff Singer of the World competition."],
            ["Ianto's Shrine", "A fan-created memorial to the character Ianto Jones from the TV show *Torchwood*, located in Cardiff Bay."],
            ["Wales Millennium Centre", "An iconic performing arts centre in Cardiff Bay, known for its striking architecture and theatre productions."],
            ["Norwegian Church Arts Centre", "A former church now serving as an arts centre and café, once frequented by author Roald Dahl."],
            ["Principality Stadium", "Wales national stadium, hosting major rugby and football matches as well as concerts and events."],
            ["Cardiff City Stadium", "The home ground of Cardiff City Football Club and the Wales national football team."],
            ["Cardiff Bay Yacht Club", "A sailing and water sports club located on the scenic waterfront of Cardiff Bay."],
            ["Techniquest (Science Centre)", "A hands-on science and discovery centre for children and families in Cardiff Bay."],
            ["Principality Stadium Tours", "A behind-the-scenes tour of the iconic stadium, including the pitch, locker rooms, and VIP areas."],
            ["National Museum Cardiff", "A major museum with art, natural history, and archaeology collections, located in the city centre."],
            ["St Fagans Castle", "A 16th-century manor house and part of the St Fagans National Museum of History, showcasing Welsh life."],
            ["Castell Coch", "A fairytale-like 19th-century Gothic Revival castle set on ancient foundations, located north of Cardiff."],
            ["Caerphilly Castle", "One of the largest castles in the UK, featuring expansive moats and medieval architecture."],
            ["Llandaff Cathedral", "An ancient and active Anglican cathedral located in the historic Llandaff district of Cardiff."],
            ["St Davids Metropolitan Cathedral", "The Roman Catholic cathedral of Cardiff, known for its stunning interior and music."],
            ["Bute Park", "A vast public park next to Cardiff Castle, ideal for walking, cycling, and enjoying nature in the city."],
            ["Roath Park", "A Victorian park with a large boating lake, conservatory, and beautiful gardens."],
            ["Victoria Park", "A family-friendly park with playgrounds, splash pads, and green spaces in west Cardiff."],
            ["Cefn Onn Park", "A landscaped country park with woodland trails and ornamental gardens in the north of Cardiff."],
            ["Cardiff Bay Wetlands Reserve", "A protected nature area supporting birds and aquatic wildlife, offering walking paths and views."],
            ["Cardiff Bay Barrage", "A sea barrier with a pedestrian and cycle path linking Cardiff Bay to Penarth, offering scenic views."],
            ["Wales National War Memorial", "A Grade I listed war memorial in Cathays Park, commemorating Welsh soldiers who died in wars."],
            ["Crowd Building (Old)", "A historic building in Cardiff, previously a notable hub—exact location or current status may vary."],
            ["St. Lythans Burial Chamber", "A Neolithic dolmen over 6,000 years old, located in the Vale of Glamorgan, just outside Cardiff."],
            ["Tinkinswood Burial Chamber", "A well-preserved Neolithic tomb with one of the largest capstones in Britain, near Cardiff."],
            ["Nantgarw China Works & Museum", "A museum celebrating fine porcelain production and local history in the village of Nantgarw."],
            ["Tommy Cooper Statue", "A statue commemorating the famous Welsh comedian, located in his hometown of Caerphilly."],
            ["Old Bishops Palace", "Ruins of a historic residence of the Bishops of Llandaff, located near the cathedral."],
            ["Insole Court", "A restored Victorian Gothic mansion with gardens and a café, open to the public in west Cardiff."],
            ["Barry Castle", "A small ruined medieval castle located in Barry, south of Cardiff, with views over the Bristol Channel."]
        ]

    if user_input_sub == "View Full Cardiff Points of Interest List":
        
        header_list = ['Point of Interest','Description of Point of Interest']
        tabulate_data = point_of_interest_list

        # print tabulate output to screen
        print('')    
        print_data_tabulate(header_list, tabulate_data)
        print('')

    else:
 
        # request sub menu option
        print(f'\n\nTwo selection to follow, first is the Starting point of interest, and the second being the destination point of interest\n\n')

        user_input_1 = display_options(point_of_interest_list, 'Points of Interest Selection (Start From)', 'point of interest option')
        user_input_2 = display_options(point_of_interest_list, 'Points of Interest Selection (Travel To)', 'point of interest option')

        #update userinput to list value
        for i, poi in enumerate(point_of_interest_list):
            if poi[0] == user_input_1:
                user_input_1 = i
            elif poi[0] == user_input_2:
                user_input_2 = i

        rout.run_dijkstra(poi_hs_table, user_input_1, user_input_2)

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

        if demo_sub == "Algorithm sort tester":
            multi.run_alg_tester()
            #exec(open("muti_processing.py").read())

        else:
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