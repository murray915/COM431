import file_data as fd
import json
import point_of_interest as poi
import random as rd

import menu_tree as mt
import user_inputs as ui
import hashtable as hs

def main():

    rootnode = mt.build_menu_tree()
    main_menu = mt.get_main_menu(rootnode)

    exit = True
    poi_hs_table = hs.Hashmap(100)

    # get test data
    poi_hs_table = create_test_pois(poi_hs_table, 15)

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

                # if not isinstance(output_list, hs):
                #     print('')
                #     print(output_list)
                #     print('')

                #     for i in output_list:
                #         print(i.poi_attribute('name'))
                #         poi_hs_table.put(i.poi_attribute('name'),i)

                #     print('')
                #     print(poi_hs_table.search_in_chunks('items'))

def create_test_pois(poi_hs_table: object, max_test_poi: int) -> object:

    random_words = [
        "apple", "river", "table", "light", "stone", "dream", "forest", "cloud", "window", "travel",
        "mirror", "clock", "pencil", "glass", "music", "sunset", "garden", "ocean", "rocket", "planet",
        "storm", "mountain", "desert", "school", "friend", "butter", "laptop", "keyboard", "camera", "puzzle",
        "shadow", "helmet", "jungle", "bottle", "flame", "orange", "pillow", "circle", "guitar", "castle",
        "butterfly", "bridge", "rabbit", "monkey", "feather", "tunnel", "frozen", "ticket", "wallet", "notebook",
        "glove", "ladder", "tiger", "spider", "wagon", "drawer", "helmet", "dragon", "breeze", "lantern",
        "string", "parrot", "planet", "anchor", "harbor", "sunrise", "carpet", "jacket", "wallet", "mirror",
        "honey", "blizzard", "volcano", "cookie", "beacon", "grape", "banana", "scooter", "zipper", "rocket",
        "shovel", "violin", "garage", "lighthouse", "starfish", "igloo", "trophy", "eagle", "curtain", "candle",
        "leaflet", "helmet", "treasure", "jungle", "marble", "jigsaw", "library", "rainbow", "snowman", "unicorn",
        "chalk", "whistle", "mystery", "compass", "sketch", "lantern", "branch", "canyon", "skate", "pebble",
        "lemon", "waffle", "thunder", "island", "hammer", "balloon", "blanket", "chimney", "ladder", "napkin",
        "squirrel", "yogurt", "raindrop", "paint", "marker", "breeze", "fabric", "trumpet", "tulip", "melon",
        "giraffe", "necklace", "spoon", "penguin", "stream", "button", "crayon", "castle", "battery", "reed",
        "calendar", "lantern", "velvet", "shoelace", "kettle", "cheese", "basket", "breeze", "magnet", "thread"
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
        "Museum","Art Gallery","Historical Site","Monument",
        "Landmark","Park","National Park","Garden","Beach","Mountain","Scenic Viewpoint","Zoo",
        "Aquarium","Castle","Fortress","Cathedral","Church","Mosque","Temple","Library","University","Market",
        "Shopping Mall","Theater","Cinema","Music Venue","Nightclub","Restaurant","Cafe","Bar","Brewery","Winery",
        "Street Art Location","Statue","Fountain","Bridge","Harbor","Lighthouse","Amusement Park",
        "Water Park","Sports Stadium","Arena","Convention Center","Town Square","Cultural Center",
        "Memorial","Botanical Garden","Wildlife Sanctuary","Trailhead","Bike Trail","Campground",
        "Observatory","Hot Spring","Cave","Volcano","Island","Village","Old Town","Embassy",
        "Government Building","Railway Station","Airport","Ferry Terminal","Marina","Visitor Center",
        "Tourist Information Office","UNESCO World Heritage Site"
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

        name = random_words[rd.randrange(0 ,149)]
        var_type = poi_types[rd.randrange(0 ,67)]
        desc = poi_descriptions[rd.randrange(0 ,39)]
        poi_id = poi_hs_table.get_next_index()
        quest = []

        for _ in range(1, rd.randrange(2 ,5)):            
            question = "quest:::"+poi_questions[rd.randrange(0 ,39)]
            
            if rd.randrange(0 , 9) >= 5:
                ans = "ans==="+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))+str(rd.randrange(0,2000))
            else:
                ans = ''

            quest.append([question,ans])

        print(f'test poi added in temp_mem {poi_id} :: {name}')
        poi_hs_table.put(name,poi.point_of_interest(poi_id, name, var_type, desc, quest))    
   
    return poi_hs_table


def saved_test_crap():    

    load_list = actfile.load_data_from_file(filepath, 10, 15)

    for i in load_list:
        i.update_id(poi_hs_table.get_next_index())
        poi_hs_table.put(i.poi_attribute('name'),i)
    

    filename = 'combine_testfile.json'
    filepath = dirname+'/data/'+filename

    actfile.save_to_file(poi_hs_table, filepath)

    # Opening JSON fileW
    with open(filepath) as f:
        data = json.load(f)

        print(data['meta_data'])

        for i in data['data']:
            print(i)

    print(f'\n\n\n\n')




main()


if __name__ == '__main__':
    import os

    poi_hs_table = hs.Hashmap(100)
    actfile = fd.data_file()

    # get test data
    poi_hs_table = create_test_pois(poi_hs_table, 50)

    # get paths
    dirname = os.path.dirname(__file__)
    filepath = dirname+'/data/'
    
    print(poi_hs_table.search_in_chunks('values'))

    actfile.save_to_file(poi_hs_table, filepath+'test.json')


    #list_obj = poi_hs_table.search_in_chunks('values')
    
    #for i in list_obj:
    #    print(i.poi_attribute('name'))
        #print(i.poi_attribute('items'))

    #print(poi_hs_table.get_value('Hello-9'))