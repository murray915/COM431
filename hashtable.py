class Hashmap():

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.next_index = 0
        self.chunks = [[] for _ in range(capacity)]

    def __len__(self):
        return self.size

    def get_next_index(self):
        return self.next_index +1
    
    def __contains__(self, key) -> bool | int:
        """ check if key in table, return bool """
        index = self.hash_function(key)
        chunk = self.chunks[index]
        counter = 0

        for k, v in chunk:
            if k == key:
                counter +=1
                returnval = True          
        
        if returnval:
            return counter
        else:
            return False
    
    def put(self, key, value) -> None:
        """ check if key in table, if true update, else insert """
        index = self.hash_function(key)
        chunk = self.chunks[index]

        chunk.append((key, value))
        self.size +=1
        self.next_index +=1

    def get_value(self, key) -> bool | list:
        """ check if key in table, if true return k, v else return bool """
        index = self.hash_function(key)
        chunk = self.chunks[index]
        output_list = []

        for k, v in chunk:
            
            if k == key:
                
                if self.__contains__(key) >= 2:
                    output_list.append(v)
                else:
                    return v

        if output_list:
            return output_list
        else:
            return False
        
    def remove_key(self, key: str, value: object) -> bool:
        """ check if key in table, if true remove k, else return bool """
        index = self.hash_function(key)
        chunk = self.chunks[index]

        if len(chunk) == 1:
            for i, (k, v) in enumerate(chunk):
                if k == key and v == value:
                    del chunk[i]
                    self.size -=1
                    self.next_index -=1

                    return True
                else:
                    return False
                
        else:
            for i, (k, v) in enumerate(chunk):
                if k == key and v == value:
                    chunk.pop(i)
                    self.size -=1
                    self.next_index -=1

                    return True
            else:
                return False
        
    def search_in_chunks(self, search_val: str) -> list | str:
        """ return key/value from user input search_val index """
        
        if search_val.lower() == "key":
            return [k for chunk in self.chunks for k, _ in chunk]
        elif search_val.lower() == "values":
            return [v for chunk in self.chunks for _, v in chunk]
        elif search_val.lower() == "items":
            return [(k, v) for chunk in self.chunks for k, v in chunk]

    def hash_function(self, key) -> int:
        """ hash map func, return hashkey """
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity

        return hash_result