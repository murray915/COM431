import file_data as fd
import json
import point_of_interest as poi
import random as rd

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

test()