"""
https://leetcode.com/problems/remove-linked-list-elements/
Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        """
        Time Complexity O(N) and Space Complexity O(1)
        """
        if not head: return head
        while head and head.val == val: head = head.next
        current = head
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else: current = current.next
        return head
        
                