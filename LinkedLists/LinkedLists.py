class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
    
    def add_begin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    
    def reverse(self):
            current_node = self.head
            prev_node = None
            while current_node:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node=current_node
                current_node = next_node
            self.head = prev_node


    def remove_data(self, data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
        else:
            while current_node:
                if current_node.data == data:
                    break
                prev_node = current_node
                current_node = current_node.next
            if current_node == None:
                return
            prev_node.next = current_node.next
            current_node = None
        
        

# Example usage:
sll = SinglyLinkedList()
sll.add_node(1)
sll.add_node(2)
sll.add_node(3)
sll.reverse()
sll.display()