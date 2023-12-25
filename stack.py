class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else :
            return "stack is empty"
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "stack is empty"
        
#instantiate stack class
my_stack = Stack()

#push elements
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.pop()) #should be 3
print(my_stack.peek()) #should be 2
print(my_stack.size()) #should be 2