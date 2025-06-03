import json
from datetime import datetime

class data_file():

    def __init__(self):
        self.meta_data = self.get_meta_data()
        self.data = self.load_data_from_file()

    def get_meta_data(self):

        try:
            with open('test.json') as f:
                data = json.load(f)
                count = len(data['data'])
                last_modified = data['meta_data']['Last Modified']

        except:
            count = 0
            last_modified = 'null'

        meta_data = {
            "Last Modified": last_modified,
            "Stored data count": count
        }

        return meta_data

    def load_data_from_file(self):
        data = []

        try:
            with open("test.json", "rt") as file:
                df = json.loads(file.readlines()[0])
                for i in df["data"]:
                    data.append(point_of_interest(i["reg"], i["type"]))
        except:
            pass

        return data

    def save_to_file(self):

        try: 
            with open('test.json') as f:
                data = json.load(f)
                count = len(data['data']) + 1

            self.meta_data = {"Last Modified": str(datetime.now()), "Stored data count": count}

        except:
            self.meta_data = {"Last Modified": str(datetime.now()), "Stored data count": 1}

        with open("test.json", "wt") as file:     
            file.write(json.dumps(self.__dict__, default=obj_dict))


    def add_car(self, car):
        try:
            self.data.append(car)
            return True
        except:
            return False
    

def obj_dict(obj):
    return obj.__dict__


class point_of_interest:

    def __init__(self, reg, type):
        self.reg = reg
        self.type = type


star = data_file()

one = point_of_interest("Hello","Piss00001")
star.add_car(one)
star.save_to_file()


# Opening JSON file
with open('test.json') as f:
    data = json.load(f)

    print(data['meta_data'])

    for i in data['data']:
        val_1 = i['reg']
        val_2 = i['type']
        print(f' Value {val_1} and the other one {val_2}')