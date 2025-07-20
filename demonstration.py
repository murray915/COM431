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
        ori_list.append(rd.randrange(0,1000))

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

def demo_stack():
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
    

def demo_queue():
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

    
def demo_muti_branch_tree():
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

    poi_long_lant = [
        [35.687,139.7495],[-6.175,106.8275],[28.61,77.23],[23.13,113.26],[19.0761,72.8775],[14.5958,120.9772],[31.2286,121.4747],[-23.5504,-46.6339],[37.5667,126.9833],[19.4333,-99.1333],
        [22.5675,88.37],[30.0444,31.2358],[24.86,67.01],[23.7289,90.3944],[40.6943,-73.9249],[39.9067,116.3975],[13.7525,100.4942],[22.5415,114.0596],[55.7506,37.6175],[-34.6036,-58.3814],
        [6.455,3.3841],[12.9789,77.5917],[10.7756,106.7019],[34.6939,135.5022],[30.66,104.0633],[41.0136,28.955],[35.6889,51.3897],[-4.3219,15.3119],[-22.9111,-43.2056],[13.0825,80.275],
        [34.2611,108.9422],[31.5497,74.3436],[29.5637,106.5504],[34.1141,-118.4068],[51.5072,-0.1275],[48.8567,2.3522],[35.1038,118.3564],[23.4,88.5],[11.7011,9.3419],[-32.9306,151.7542],[39.1336,117.2054],
        [-12.06,-77.0375],[14.2504,32.98],[23.25,88.43],[30.267,120.153],[35.1833,136.9],[-8.8383,13.2344],[23.0214,113.1216],[3.1686,101.698],[42.4414,19.2628],[15.1458,120.9783],[24.8833,68.8167],[30.62,74.25],
        [35.3669,132.7547],[31.287,34.2595],[35.7367,-0.5542],[58.05,38.8333],[-9.3,14.95],[-6.3704,106.8176],[38.697,-9.3017],[-26.1,28.2333],[33,-7.6167],[6.5436,-7.4933],[38.75,-9.2333],
        [38.1125,-122.2342],[53.1333,26.0167],[35.991,-79.9937],[32.03,44.4],[-7.1908,-48.2069],[36.8931,126.6281],[11.9401,79.4861],[20.95,72.93],[9.7897,125.4958],[39.0311,43.3597],
        [38.1144,15.65],[7.7333,8.5],[11.5481,107.8075],[33.5833,71.4333],[19.124,-72.4817],[33.7787,-117.9601],[26.0128,-80.3382],[37.9667,34.6792],[-28.232,30.566],[13.7833,-89.1167],
        [14.2978,-90.7869],[4.3452,-74.3618],[34.3,48.8178],[53.7778,20.4792],[42.6333,141.6],[6.9333,1.6833],[20.61,72.926],[22.7528,-102.5078],[34.6935,-118.1753],[23.8494,57.4386],
        [15.3249,120.6554],[-33.3,-66.3333],[-22.5439,-44.1708],[5.1,-1.25],[0.8303,-77.6444],[4.1354,32.2869],[3.3194,99.1522],[35.6539,139.9022],[40.0077,-75.1339],[43.7417,-79.3733],
        [34.764,113.684],[30.8372,106.1106],[36.6702,117.0207],[29.987,31.2118],[59.9375,30.3086],[23.551,116.3727],[37.436,116.359],[19.2833,-98.4333],[5.5333,-73.3667],
        [54.9,52.3],[10.6204,-84.512],[-21.7878,-46.5608],[28.6981,77.0689],[33.5606,35.3758],[-6.2667,106.4667],[7.7,27.99],[40.3139,36.5542],[37.8947,127.2002],[36.8667,6.9],
        [41.5495,-72.0882],[31.802,74.255],[30.0694,71.1942],[37.3057,-120.4779],[-34.45,-58.5667],[53.0167,158.65],[49.4167,8.7167],[53.645,-1.7798],[33.9517,131.2467],
        [41.4667,69.5833],[30.5567,49.1897],[37.9125,28.3206],[42.9848,-71.4447],[31.8801,-102.3448],[52.3833,4.6333],[28.228,112.939],[33.963,118.275],[21.5428,39.1728],
        [34.5206,109.471],[52.52,13.405],[17.95,-76.8799],[41.9844,2.8211],[45.1715,5.7224],[30.1997,31.2053],[10.53,123.93],[37.3448,126.9683],[-13.1333,28.4]
    ]

    poi_locations = [
        "Japan","Indonesia","India","China","India","Philippines","China","Brazil","Korea, South","Mexico","India","Egypt","Pakistan",
        "Bangladesh","United States","China","Thailand","China","Russia","Argentina","Nigeria","India","Vietnam","Japan","China","Turkey","Iran","Congo (Kinshasa)",
        "Brazil","India","China","Pakistan","China","United States","United Kingdom","France","China","India","Nigeria","Australia","China","Peru","Sudan",
        "India","China","Japan","Angola","China","Malaysia","Montenegro","Philippines","Pakistan","India","Japan","Gaza Strip","Algeria","Russia","Angola",
        "Indonesia","Portugal","South Africa","Morocco","Ca te dae Ivoire","Portugal","United States","Belarus","United States","Iraq","Brazil","Korea, South","India","India","Philippines","Turkey","Italy",
        "Nigeria","Vietnam","Pakistan","Haiti","United States","United States","Turkey","South Africa","El Salvador","Guatemala","Colombia",
        "Iran","Poland","Japan","Benin","India","Mexico","United States","Oman","Philippines","Argentina","Brazil","Ghana","Colombia","South Sudan","Indonesia","Japan","United States","Canada","China",
        "China","China","Egypt","Russia","China","China","Mexico","Colombia","Russia","Costa Rica","Brazil","India","Lebanon","Indonesia","South Sudan","Turkey","Korea, South","Algeria","United States",
        "Pakistan","Pakistan","United States","Argentina","Russia","Germany","United Kingdom","Japan","Uzbekistan","Iran","Turkey","United States",
        "United States","Netherlands","China","China","Saudi Arabia","China","Germany","Jamaica","Spain","France","Egypt","Philippines","Korea, South","Zambia",
    ]
    
    for _ in range(0, max_test_poi):

        name = points_of_interest[rd.randrange(0 ,len(points_of_interest))]
        var_type = poi_types[rd.randrange(0 ,len(poi_types))]
        desc = poi_descriptions[rd.randrange(0 ,len(poi_descriptions))]
        poi_id = poi_hs_table.get_next_index()
        quest = []

        location_details = rd.randrange(0 ,len(poi_descriptions))
        long_and_lang = poi_long_lant[location_details]
        location = poi_locations[location_details]
    
        for _ in range(1, rd.randrange(2 ,5)):            
            question = poi_questions[rd.randrange(0 ,39)]
            
            # if rd.randrange(0 , 9) >= 5:
            #     ans = str(rd.randrange(0,2000))+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))
            # else:
            #     ans = ''

            ans = ''
            quest.append([question,ans])

        print(f'Point of Interest added into application: \n\tPOI ID : {poi_id}  \n\tPOI Name : {name} \n\tPOI Description : {desc}')
        poi_hs_table.put(name,poi.point_of_interest(poi_id, name, var_type, desc, quest, location, long_and_lang))    
   
    return poi_hs_table


#runset = 'quicksort'
#runset = 'merge_sort'
#runset = 'bubble_sort'
#print_cons = True
#ori_list = get_data_arr()
#demo_sorting_algr(ori_list, print_cons, runset)

#demo_queue()
#demo_stack()
#demo_menu_tree()
