class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
        """
        1 2 3 4 5
    cur         ^     
            ^ 
        """
        dump = ListNode(0)
        dump.next = head
        
        fast = dump
        slow = dump
        
        while n+1:
            fast = fast.next
            n -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dump.next

def printingValues(head):
    while head:
        print(head.val)
        head= head.next
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
f = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = f

print(printingValues(removeNthFromEnd(a, 2)))
            
        