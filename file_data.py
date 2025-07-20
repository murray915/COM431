import json
from datetime import datetime
import point_of_interest as poi
import hashtable as hs

class data_file():

    def __init__(self):
        self.meta_data = {"Last Modified": str(datetime.now()), "Stored data count": 0}
        self.data = self.load_data_from_file()

    def load_data_from_file(self, fullpath = None) -> list:
        """ Load existing file (non-user input) """
        try:
            if fullpath:
                load_data = []

                with open(fullpath, "rt") as file:
                    df = json.loads(file.readlines()[0])
                    for i in df["data"]:
                        load_data.append(poi.point_of_interest(i["id"], i["name"], i["poi_type"], i['desc'], i['quest'],i['location'],i['longandlat'])) 
               
                return load_data
            
        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
            return False       
    
    def save_to_file(self, load_data = None, fullpath = None) -> bool:
        """ Save user session data to input fullpath """
        self.meta_data = {"Last Modified": str(datetime.now()), "Stored data count": len(load_data)}
        self.data = load_data.search_in_chunks("values")

        try:
            with open(fullpath, "wt") as file:     
                file.write(json.dumps(self.__dict__, default=obj_dict))
            
            return True
        
        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
            return False

    def view_json_file(self, filepath: str):
        """ load and print json file to console """
        
        with open(filepath, "r") as file:
            df = json.loads(file.readlines()[0])

        print(json.dumps(df, indent=4))
        return 


def obj_dict(obj):
    return obj.__dict__