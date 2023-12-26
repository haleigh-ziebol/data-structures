class Queue:
    def __init__(self):
        self.queue = []
       
    def is_empty(self):
        return len(self.queue) == 0
   
    def size(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print(my_queue.dequeue()) # should print 1
print(my_queue.front()) # should print 2
my_queue.enqueue(4)
print(my_queue.size()) # should be 3