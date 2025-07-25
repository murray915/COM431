class Stack:
    def __init__(self):
        self.stack = []

    def isempty(self) -> bool:
        """ check if stack is empty """
        if len(self.stack) == 0:
            return True
        return False

    def stack_size(self) -> int:
        """ return size of stack """
        if self.isempty():            
            return 0
        return len(self.stack)
    
    def stack_top_data(self) -> str | bool:
        """ return the last data input on stack """
        if self.isempty():
            print('Stack is empty')
            return False
        return self.stack[-1]

    def stack_all_data(self) -> str | bool:
        """ return the last data input on stack """
        if self.isempty():
            print('Stack is empty')
            return False
        return self.stack
    
    def stack_add(self, data) -> bool:
        """ add data to stack """        
        self.stack.append(data)
        return True
    
    def stack_remove(self) -> bool:
        """ remove last data from stack """
        if self.isempty():
            print('Stack is empty')
            return False
        
        self.stack.pop()
        return True

    def print_queue(self):
        """ print values within stack """
        print(f'Stack Metrics:')
        print(f'\tTotal size of the stack is {len(self.stack)}')
        
        if len(self.stack) == 0:
            print(f'\tNext value to remove (pop) is : None')
        else:
            print(f'\tNext value to remove (pop) is : {self.stack_top_data()}')
        
        print(f'The contents of the stack is: ')        
        
        if len(self.stack) == 0:
            print(f'\tStack is empty')
        else:
            for i in range(len(self.stack)):
                print(f'\tAt index: {i} : {self.stack[i]}')