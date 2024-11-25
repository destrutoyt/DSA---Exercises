class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(values):
    """Converts a Python list to a linked list and returns the head."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def middleNode(head):
    slow_p = head
    fast_p = head
    while fast_p is not None and fast_p.next is not None:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
    return slow_p

# Example Usage
values = [1, 2, 3, 4, 5]  # Example list
head = list_to_linked_list(values)  # Convert to linked list
middle = middleNode(head)  # Find middle node
print(middle.val)  # Output the value of the middle node
