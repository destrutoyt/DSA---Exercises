"""
LINKED LIST EXPLANATION:
Train Example:
Nodes: Data are the wagons of the train
Next: These are the chains connection to the NEXT wagon (node)
Head: This would be the wagon (node) where the train driver would be found (In other words, the first element/node of the list)
Tail: The LAST wagon of the train (In other words, the last element/node of the list)

"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
    
    def length(self):
        current_node = self.head
        total = 0
        while current_node.next:
            total += 1
            current_node = current_node.next
        return total
    
    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.data)
        print(elems)
    
    def get(self, index):
        if index >= self.length():
            print("Error: 'Get' Index out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            else:
                current_index += 1
                
    def erase(self, index):
        if index >= self.length():
            print("Error: 'Get' Index out of range!")
            return None
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1

my_list = LinkedList()
my_list.append(1)
my_list.append(3)
my_list.append(2)
my_list.display()
print(f"Element at 1nd index: {my_list.get(1)}")
my_list.erase(1)
my_list.display()