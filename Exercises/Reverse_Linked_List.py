"""
PROBLEM: Given the head of a singly linked list, reverse the list, and return the reversed list.
SOLUTION: We are using an iterative approach on a Singly Linked List
"""
def reverseList(head):
    prev = None
    cur = head

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev
