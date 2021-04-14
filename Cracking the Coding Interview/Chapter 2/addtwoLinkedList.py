"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [2,4,3], l2 = [5,6,9]
Output: [7,0,3,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2):
    dummy = ListNode(-1)
    cur = dummy
    carry = 0
    while l1 or l2:
        valFirst = l1.val if l1 else 0
        valSecond = l2.val if l2 else 0
        temp = ListNode(valFirst + valSecond + carry)
        temp.val, carry = temp.val % 10, temp.val // 10
        cur.next = temp
        cur = cur.next
        if l1 is not None: l1 = l1.next  
        if l2 is not None: l2 = l2.next 
    if carry != 0: cur.next = ListNode(carry)
    return dummy.next
def printing(head):
    while head:
        print(head.val)
        head = head.next
a = ListNode(2)
b = ListNode(4)
c = ListNode(3)
a.next = b
b.next = c

d = ListNode(5)
f = ListNode(6)
h = ListNode(9)
d.next = f
f.next = h
print(printing(addTwoNumbers(a, d)), ":Ignore the last None part because it's just looping through the linkedlist and then printing it")