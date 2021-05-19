"""
Write code to partition a linked list around a value x, such that all nodes less than x 
come before all nodes greater than or equal to x. (Important: The partition element
x can appear anywhere in the "right partition"; it does not need to appear between
the left and right partitions. The additional spacing the example below indicates the 
partition.)
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def parition(head, x): 
    before = before_base = ListNode(-1)
    after = after_base = ListNode(-1)
    while head:
        if x > head.val:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_base.next
    return before_base.next

def pritingLinkedList(head):
    while head: 
        print(head.val)
        head = head.next

a = ListNode(3)
b = ListNode(5)
c = ListNode(8)
d = ListNode(5)
e = ListNode(10)
f = ListNode(2)
g = ListNode(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
mergedList = parition(a, 5)
print(pritingLinkedList(mergedList))