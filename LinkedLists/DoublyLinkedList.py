class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = DoublyNode(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
    
    def display_forward(self):
        current_node = self.head ## set to head for start
        while current_node:
            print(current_node.data, end= " <-> ")
            current_node = current_node.next
        print("None")

    def display_backward(self):
        current_node = self.head ## set to head for start
        while current_node.next:
            current_node = current_node.next
        while current_node:
            print(current_node.data, end= " <-> ")
            current_node = current_node.prev
        print("None")

## start new Doubly Linked List
dll = DoublyLinkedList()

# add nodes to list
dll.add_node(1)
dll.add_node(2)
dll.add_node(3)

#display list in both directions
dll.display_backward()
dll.display_forward()