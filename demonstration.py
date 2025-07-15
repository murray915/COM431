import random as rd
import time
import sorting_algs as algs
import queue_class as qc
import stack_class as sc
import menu_tree as mt
import point_of_interest as poi

def get_data_arr(top_range = 15) -> list:
    """ return large random array ; input top random size """
    ori_list = []
    for _ in range(0, rd.randrange(10,top_range)):
        ori_list.append(rd.randrange(0,10000))

    return ori_list


def demo_sorting_algr(ori_list, print_cons, runset):
    """ demo sorting algr ; input sorting algr name """
    start_time = time.time()

    if print_cons:
        print("-----------------------------------------------------------------")
        print(f'Length of list: {len(ori_list)}, action on runset {runset}:\nOriginal list: \n {ori_list}')
        print(f"-----------------------------------------------------------------\n\n")

    try:
        # set runset as varible function
        func = getattr(algs, runset)

        # Call runset
        if "quicksort" in runset:
            func(ori_list, 0, len(ori_list) -1, print_cons)
        else:
            func(ori_list, print_cons)
            
    except Exception as err: # Exception Block. Return data to user & False
        print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")

    if print_cons:
        print(f'----------------------------------------------------------------- \nFinal Output value list: \n {ori_list}')
        print("  --- Run completed in %s seconds ---" % (time.time() - start_time))
        print("-----------------------------------------------------------------")

def demo_stack_data_type():
    """ demo sorting algr ; input sorting algr name """
    demo_stack = sc.Stack()

    print(f'Demo for Stack, random add / remove actions and results')

    for _ in range(1, rd.randrange(2,8)):
        num = rd.randrange(1,8)        
        print(f'\tadd to stack {num}')
        demo_stack.stack_add(num)

    for _ in range(1, rd.randrange(2,5)):      
        print(f'\tremove from stack')
        demo_stack.stack_remove()

    demo_stack.print_queue()
    

def demo_queue_data_type():
    """ demo sorting algr ; input sorting algr name """
    demo_que = qc.Queue(8)

    print(f'Demo for queue, random enqueue / dequeue actions and results')

    for _ in range(1, rd.randrange(2,8)):
        num = rd.randrange(1,8)        
        print(f'\tadd to queue {num}')
        demo_que.enqueue(num)

    for _ in range(1, rd.randrange(2,5)):      
        print(f'\tdequeue')
        demo_que.dequeue()

    demo_que.print_queue()

def build_product_tree_demo_001():
    root = mt.TreeNode("Electronics","All items within electronics")

    # depth 2 menu option
    laptop = mt.TreeNode("Laptop","Laptop Brands selection")
    laptop.add_child(mt.TreeNode("Mac","Apple laptop"))
    laptop.add_child(mt.TreeNode("Surface","Surface laptop"))
    laptop.add_child(mt.TreeNode("Thinkpad","Thinkpad, notepad"))
    root.add_child(laptop)

    # depth 3 menu option
    # Sub menu
    keyboard = mt.TreeNode("keyboard","Keyboard Brands selection")
    keyboard.add_child(mt.TreeNode("razor","Razor brand keyboards"))
    keyboard.add_child(mt.TreeNode("steelseries","Steelseries brand keyboards"))
    laptop.add_child(keyboard)   

    # depth 2 menu option
    cellphone = mt.TreeNode("Cell Phone","Phone Brands selection")
    cellphone.add_child(mt.TreeNode("iPhone","iPhone (mac) phone"))
    cellphone.add_child(mt.TreeNode("Google Pixel","Google (android) phone"))
    cellphone.add_child(mt.TreeNode("Vivo","Vivo (android) phone"))
    root.add_child(cellphone)

    # depth 2 menu option
    tv = mt.TreeNode("TV","TV Brands selection")
    tv.add_child(mt.TreeNode("Samsung","Samsung TVs import"))
    tv.add_child(mt.TreeNode("LG","LG TVs import"))
    root.add_child(tv)

    return root

def build_product_tree_demo_002():
    root = mt.TreeNode("Menu Option","n/a")

    # depth 2 menu option
    laptop = mt.TreeNode("Sub Menu 1","n/a")
    laptop.add_child(mt.TreeNode("Option 1","Descript - 1"))
    laptop.add_child(mt.TreeNode("Option 2","Descript - 2"))
    laptop.add_child(mt.TreeNode("Option 3","Descript - 3"))
    root.add_child(laptop)

    # depth 3 menu option
    # Sub menu
    keyboard = mt.TreeNode("Sub sub-menu ","n/a")
    keyboard.add_child(mt.TreeNode("Option 1","Descript - 1"))
    keyboard.add_child(mt.TreeNode("Option 2","Descript - 2"))
    laptop.add_child(keyboard)   

    # depth 2 menu option
    cellphone = mt.TreeNode("Sub Menu 2","n/a")
    cellphone.add_child(mt.TreeNode("Option 1","Descript - 2"))
    cellphone.add_child(mt.TreeNode("Option 2","Descript - 2"))
    cellphone.add_child(mt.TreeNode("Option 3","Descript - 2"))
    root.add_child(cellphone)

    return root

    
def demo_menu_tree():
    """ demo tree menu """
    rootnode002 = build_product_tree_demo_002()
    rootnode001 = build_product_tree_demo_001()

    print('')
    rootnode001.print_tree()
    print('')
    rootnode002.print_tree()
    print('')

    output = rootnode001.get_child_data("Laptop")

    print(f'"Laptop" sub-menu option & description print ; returned data as list -> \n\n{output}\n\nReturned menu option & Desc for menu printouts to users :')
    for i in output:
        print(f'\tMenu Option : {i[0]} \t\tmenu description : {i[1]}')
    
    print('')

def create_test_pois(poi_hs_table: object, max_test_poi: int) -> object:
    """ create number of POIs from input int value """

    points_of_interest = [
        "Eiffel Tower", "Statue of Liberty", "Great Wall of China", "Machu Picchu", "Colosseum",
        "Taj Mahal", "Christ the Redeemer", "Stonehenge", "Grand Canyon", "Niagara Falls",
        "Mount Everest", "Pyramids of Giza", "Sydney Opera House", "Big Ben", "Tokyo Tower",
        "Acropolis of Athens", "Petra", "Burj Khalifa", "Louvre Museum", "Times Square",
        "Central Park", "Golden Gate Bridge", "Mount Fuji", "Santorini", "Banff National Park",
        "Yellowstone National Park", "Yosemite National Park", "Redwood National Park", "Victoria Falls", "Angel Falls",
        "Great Barrier Reef", "Serengeti National Park", "Galápagos Islands", "Antelope Canyon", "Alhambra",
        "Mont Saint-Michel", "Neuschwanstein Castle", "Prague Castle", "Brandenburg Gate", "Berlin Wall",
        "Versailles Palace", "Buckingham Palace", "Tower of London", "St. Peters Basilica", "Vatican Museums",
        "Sagrada Familia", "Park Güell", "La Rambla", "Leaning Tower of Pisa", "Trevi Fountain",
        "The Shard", "Empire State Building", "Brooklyn Bridge", "Chicago Riverwalk", "CN Tower",
        "Banaras Ghats", "Meenakshi Temple", "Amber Fort", "Red Fort", "Qutub Minar",
        "Gateway of India", "Marina Beach", "Charminar", "Hampi Ruins", "Ajanta Caves",
        "Borobudur Temple", "Ubud Monkey Forest", "Ha Long Bay", "Angkor Wat", "Bagan Temples",
        "Blue Lagoon", "Reykjavik Church", "Thingvellir National Park", "Geysir", "Skógafoss",
        "Plitvice Lakes", "Dubrovnik Old Town", "Diocletians Palace", "Lake Bled", "Matterhorn",
        "Zermatt", "Lake Geneva", "Château de Chillon", "Lake Como", "Cinque Terre",
        "Amalfi Coast", "Pompeii", "Mt. Vesuvius", "Blue Mosque", "Hagia Sophia",
        "Topkapi Palace", "Cappadocia", "Pamukkale", "Ephesus", "Mount Kilimanjaro",
        "Table Mountain", "Robben Island", "Cape of Good Hope", "Kruger National Park", "Victoria & Alfred Waterfront",
        "Dubai Mall", "Dubai Marina", "Palm Jumeirah", "Sheikh Zayed Mosque", "Abu Dhabi Louvre",
        "Jerusalem Old City", "Western Wall", "Dome of the Rock", "Dead Sea", "Masada",
        "Petronas Towers", "Batu Caves", "Cameron Highlands", "Marina Bay Sands", "Gardens by the Bay",
        "Sentosa Island", "Merlion Park", "Namsan Tower", "Gyeongbokgung Palace", "Jeju Island",
        "Great Ocean Road", "Twelve Apostles", "Uluru", "Bondi Beach", "Fraser Island",
        "Christchurch Botanic Gardens", "Milford Sound", "Hobbiton Movie Set", "Rotorua Geothermal Park", "Queenstown",
        "Chichen Itza", "Tulum Ruins", "Teotihuacan", "Cancún Beaches", "Frida Kahlo Museum",
        "Christ the Redeemer", "Iguazu Falls", "Sugarloaf Mountain", "Copacabana Beach", "Amazon Rainforest",
        "Cusco", "Sacred Valley", "Nazca Lines", "Lake Titicaca", "Arequipa",
        "Moai Statues of Easter Island", "Mount Rushmore", "Walt Disney World", "Universal Studios", "Smithsonian Institution"
    ]

    poi_questions = [
        "What are the top attractions nearby?","Are there any historical sites in this area?",
        "Where can I find the best local food?","Is there a museum close to here?","What are the best places to take photos around here?", "Are there any guided tours available?",
        "Can you recommend a good park or garden nearby?","Where is the nearest shopping district?",
        "What are the must-see landmarks in this city?","Are there any famous buildings in this area?",
        "Is there a scenic viewpoint or lookout spot here?","What cultural events are happening nearby?",
        "Are there any popular festivals this week?","Can I find any art galleries close to here?",
        "What are the best nightlife spots around?","Is there a local market I should visit?","Where can I try traditional cuisine?","Are there any UNESCO World Heritage sites nearby?",
        "Is there a place to rent bikes or scooters?","Are there any kid-friendly attractions in the area?",
        "What is the most iconic attraction here?","Are there any hidden gems most tourists miss?","Where can I get the best city view?","Are there any free attractions nearby?",
        "What time does the local museum open?","Is there a walking tour I can join today?","What are the top-rated restaurants around here?",
        "Can you suggest any romantic places nearby?","Where can I find street art or murals in this city?",
        "Are there any famous film locations here?","What are the best beach spots in this area?",
        "Are there any cultural heritage sites within walking distance?","Is there a zoo or aquarium nearby?","Are there any botanical gardens around here?",
        "Whats the oldest building in this town?","Where can I watch the sunset around here?",
        "Is there a castle or fortress nearby?","Where can I learn about the local history?",
        "Are there any local legends or folklore sites?","Is there a public square or plaza nearby?"
    ]

    poi_types = [
        "Restaurants",
        "Museums",
        "Parks",
        "Hotels",
        "Shopping Centers",
        "Theaters",
        "Historical Sites",
        "Stadiums",
        "Zoos",
        "Other"
    ] 

    poi_descriptions = [
        "A renowned museum featuring historical artifacts and exhibitions.","A peaceful park with walking trails, gardens, and open green spaces.","A historic castle offering guided tours and panoramic views.","An art gallery showcasing contemporary and classical works.",
        "A vibrant local market full of fresh produce, crafts, and street food.","An ancient temple known for its intricate architecture and spiritual significance.",
        "A scenic viewpoint overlooking the city skyline or natural landscape.","A popular beach destination ideal for sunbathing and swimming.",
        "A national park with diverse wildlife and hiking opportunities.","A bustling shopping mall with international brands and local boutiques.",
        "A lively square surrounded by cafes, shops, and street performers.","A botanical garden home to rare plants and seasonal flower displays.",
        "A world-famous landmark symbolic of the citys identity.","A family-friendly zoo with animals from all over the world.",
        "A historical monument commemorating a significant event or figure.","An aquarium featuring marine life exhibits and interactive displays.",
        "An open-air amphitheater hosting concerts and cultural events.","A charming old town with cobblestone streets and historic buildings.",
        "A lighthouse situated on the coast, offering dramatic sea views.","An iconic bridge connecting neighborhoods and offering photo ops.","A cultural center that holds exhibitions, performances, and workshops.",
        "A modern stadium hosting sports events and entertainment shows.","A hidden gem known mostly by locals, away from the tourist crowds.","An observatory where visitors can explore the night sky and space.",
        "A scenic hiking trail with waterfalls and forested paths.","A spiritual site that serves as a center for local religious practices.",
        "A vibrant nightlife district with bars, live music, and entertainment.","A castle ruin with stories of ancient battles and local legends.",
        "A colorful street filled with murals and urban art.","A marina with docked boats, waterfront cafes, and evening strolls.","A unique geological formation that attracts photographers and hikers.",
        "A ferry terminal connecting key islands and coastal towns.","An open plaza where markets, festivals, and public events are held.",
        "A university campus with historical buildings and academic museums.","A quiet village offering insight into traditional lifestyles and crafts.",
        "A museum of science and technology with interactive exhibits.",
        "A war memorial honoring soldiers and their legacy.","A traditional craft market selling handmade goods and souvenirs.",
        "A medieval fortress with battlements, towers, and dungeons.","A viewpoint popular at sunset for breathtaking photos."
    ]

    for _ in range(0, max_test_poi):

        name = points_of_interest[rd.randrange(0 ,len(points_of_interest))]
        var_type = poi_types[rd.randrange(0 ,len(poi_types))]
        desc = poi_descriptions[rd.randrange(0 ,len(poi_descriptions))]
        poi_id = poi_hs_table.get_next_index()
        quest = []

        for _ in range(1, rd.randrange(2 ,5)):            
            question = poi_questions[rd.randrange(0 ,39)]
            
            # if rd.randrange(0 , 9) >= 5:
            #     ans = str(rd.randrange(0,2000))+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))
            # else:
            #     ans = ''

            ans = ''
            quest.append([question,ans])

        print(f'Point of Interest added into application: \n\tPOI ID : {poi_id}  \n\tPOI Name : {name} \n\tPOI Description : {desc}')
        poi_hs_table.put(name,poi.point_of_interest(poi_id, name, var_type, desc, quest))    
   
    return poi_hs_table

#runset = 'quicksort'
#runset = 'merge_sort'
#runset = 'bubble_sort'
#print_cons = True
#ori_list = get_data_arr()

#demo_sorting_algr(ori_list, print_cons, runset)

#demo_queue_data_type()
#demo_stack_data_type()
#demo_menu_tree()
