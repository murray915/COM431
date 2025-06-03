
class point_of_interest:

    def __init__(self, name: str, poi_type: str, desc: str, quest: list):
        """ Main vars for the poi class """
        self.name = name
        self.poi_type = poi_type
        self.desc = desc
        self.quest = quest

    def user_ques_ans_update(self, quest: list) -> bool:
        """ Add user quest/ans to self.quest list """        
        try:
            self.quest.append(quest)            
            return True
        
        except Exception as err: # Exception Block. Return data to user & False
            print(f"\n\n** Unexpected {err=}, {type(err)=} **\n\n")
            return False