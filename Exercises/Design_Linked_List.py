class ListNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList():
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def display(self):
        elems = []
        cur = self.left.next
        while cur != self.right: 
            elems.append(cur.val)
            cur = cur.next
        return elems


    def addAtHead(self, val):
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val):
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index, val):
        cur = self.left.next
        
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, next, prev = ListNode(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev       

    def deleteAtIndex(self, index):
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2);   
myLinkedList.get(1);             
myLinkedList.deleteAtIndex(1);    
myLinkedList.get(1);      
print(myLinkedList.display())
