class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None  

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    # Task 1: Add node to the beginning
    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
            
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    # Task 2: Remove node with given data
    def remove_by_data(self, data):
        current_node = self.head
        prev_node = None

        while current_node:
            if current_node.data == data:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
                return True
            prev_node = current_node
            current_node = current_node.next
        print(f"Data {data} not found.")
        return False
    
   # Task 3: Reverse the list in-place
    def reverse_list(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

# Example usage:
sll = SinglyLinkedList()
sll.add_node(1)
sll.add_node(2)
sll.add_node(3)
# Add a value to the beginning
sll.add_to_beginning(4)
sll.display()
# Display the list before removal
print("Before removal:")
sll.display()
# Call the remove_by_data method
result = sll.remove_by_data(2)
# Display the list after removal
print("After removal:")
sll.display()
# Display the list before reversing
print("List before reversing:")
sll.display()
# Reverse the list
sll.reverse_list()
# Display the list after reversing
print("List after reversing:")
sll.display()