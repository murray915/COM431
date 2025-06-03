import json
from datetime import datetime
import point_of_interest as poi
class data_file():

    def __init__(self):
        self.meta_data = self.get_meta_data()
        self.data = self.load_data_from_file()


    def get_meta_data(self):
        """ Update / Create header meta data for json file """
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
        """ Load existing file (non-user input) """
        load_data = []

        try:
            with open("test.json", "rt") as file:
                df = json.loads(file.readlines()[0])
                for i in df["data"]:
                    load_data.append(poi.point_of_interest(i["name"], i["poi_type"], i['desc'], i['quest']))       
        except:
            pass

        return load_data


    def save_to_file(self) -> bool:
        """ Save user session data """        
        try:
            try: 
                with open('test.json') as f:
                    data = json.load(f)
                    count = len(data['data']) + 1

                self.meta_data = {"Last Modified": str(datetime.now()), "Stored data count": count}

            except:
                self.meta_data = {"Last Modified": str(datetime.now()), "Stored data count": 1}

            with open("test.json", "wt") as file:     
                file.write(json.dumps(self.__dict__, default=obj_dict))
            
            return True
        
        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
            return False


    def add_data(self, data) -> bool:
        """ Add poi (data) to existing self var """
        try:
            self.data.append(data)
            return True
        
        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
            return False
    

def obj_dict(obj):
    return obj.__dict__