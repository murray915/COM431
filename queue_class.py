
# Key notes / learning sources 
    # - https://www.youtube.com/watch?v=VFSUWEAFmy4

class Queue:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def isfull(self) -> bool:
        """ check if queue is full """
        if self.capacity == self.size:
            return True
        else:
            return False

    def isempty(self) -> bool:
        """ check if queue is empty """
        if self.size == 0:
            return True
        else:
            return False 
              
    def enqueue(self, data) -> bool:
        """ add value to tail of queue """
        if(self.isfull()):
            print("Queue is full")
            return False
            
        self.storage[self.tail] = data
        self.tail = (self.tail +1) % self.capacity
        self.size +=1

        return True

    def dequeue(self) -> str | bool:
        """ remove value from head of queue """
        if(self.isempty()):
            print("Queue is empty")
            return False
    
        data = self.storage[self.head]
        self.head = (self.head +1) % self.capacity
        self.size -= 1        
        
        return data
    
    def print_queue(self) -> bool:
        """ print values within queue """

        print(f'Queue Metrics:')
        print(f'\tCapacity of the queue is : {self.capacity}')
        print(f'\tHead of the queue is: {self.head}')
        print(f'\tTail of the queue is: {self.tail}') 
        print(f'\tTotal size of the queue is {self.size}')

        print(f'The contents of the queue is: ')        
        for i in range(len(self.storage)):
            print(f'\tAt index: {i} : {self.storage[i]}')

        return True