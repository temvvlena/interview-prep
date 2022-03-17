# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None: return None
        if l1 is None: return l2
        if l2 is None: return l1
        head = ListNode(-1)
        current = head
        while l1 and l2: 
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1 is not None:
            current.next = l1
        else: current.next = l2
        return head.next
        """
        Solved March 16, 2022

        if not list1 and not list2: return None
        cur = ListNode(-1000)
        dumb = cur
        while list1 and list2:
            if list1.val < list2.val:
                dumb.next = list1
                list1 = list1.next
            else:
                dumb.next = list2
                list2 = list2.next
            dumb = dumb.next
        if list1 is not None:
            dumb.next = list1
        else:
            dumb.next = list2
        return cur.next
        """