# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2+carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


"""
For Visualization at https://pythontutor.com/visualize.html#mode=edit

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2):
        result = ListNode(0)
        result_tail = result
        carry = 0
        
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2+carry, 10)
            
            result_tail.next = ListNode(out)
            result_tail = result_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        return result.next
a = ListNode(9)
b = ListNode(9)
c = ListNode(9)
d = ListNode(9)
e = ListNode(9)
f = ListNode(9)
g = ListNode(9)
h = ListNode(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

i = ListNode(9)
k = ListNode(9)
l = ListNode(9)
p = ListNode(9)
i.next = k
k.next = l 
l.next = p

print(addTwoNumbers(a, i))
"""
