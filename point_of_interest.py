
class point_of_interest:

    def __init__(self, poi_id: int, name: str, poi_type: str, desc: str, quest: list, location: str, longandlat: list):
        """ Main vars for the poi class """
        self.id = poi_id
        self.name = name
        self.poi_type = poi_type
        self.desc = desc
        self.quest = quest
        self.location = location
        self.longandlat = longandlat

    def user_ques_ans_update(self, quest: list) -> bool:
        """ Add user quest/ans to self.quest list """        
        try:
            self.quest = quest
            return True
        
        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
            return False

    def poi_ID_update(self, poi_id: int):
        """ Update poi id """        
        try:
            self.id = poi_id
            return True
        
        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
            return False
        
    def poi_attribute(self, attribute: str):
        """ get poi attribute """
        """ inputs :: id / name  poi_type, desc, quest, location or all """

        if attribute == 'id':
            return self.id
        elif attribute == 'name':
            return self.name
        elif attribute == 'poi_type':
            return self.poi_type
        elif attribute == 'desc':
            return self.desc
        elif attribute == 'quest':
            return self.quest
        elif attribute == 'location':
            return [self.location, self.longandlat]        
        elif attribute == 'all_exc_ques_loc':
            return self.id, self.name, self.poi_type, self.desc
        elif attribute == 'all': 
            return self.id, self.name, self.poi_type, self.desc, self.quest, self.location, self.longandlat
        
    def update_id(self, new_id: int):
        """ update id based on input """
        self.id = new_id