# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Recursively
        1 -> 2 -> 3 -> 4 -> None
        if not head or not head.next: return head
        p = self.reverseList(head.next)
        head.next.next=head
        head.next = None
        return p
        Iterate
        1 -> 2 -> 3 -> 4 -> None
        null <- 1 
        prev = None
        while not head:
            temp = head.next
            head = prev
            prev = head
            temp = head
        return prev
        """
        previousNode = None
        while head is not None:
            temp = head.next
            head.next = previousNode
            previousNode = head
            head = temp
        return previousNode
            

        
        