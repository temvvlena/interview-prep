# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Recursively
        class Solution:
            def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
                if not head or head.next is None:
                    return head
                p = self.reverseList(head.next)
                head.next.next = head
                head.next = None
                return p
        """
        previousNode = None
        while head is not None:
            temp = head.next
            head.next = previousNode
            previousNode = head
            head = temp
        return previousNode
