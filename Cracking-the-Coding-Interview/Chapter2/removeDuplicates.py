class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head):
    cur = head
    while cur and cur.next:
        temp = cur.next
        while temp and cur.val == temp.val:
            temp = temp.next
        cur.next = temp
        cur = cur.next
    return head
def printingValues(head):
    while head:
        print(head.val)
        head= head.next
a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
f = ListNode(3)
a.next = b
b.next = c
c.next = d
d.next = f

print(printingValues(deleteDuplicates(a)))