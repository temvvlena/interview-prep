"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Remove Duplicates from Sorted List II
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Input: head = [1,1,1,2,3]
Output: [2,3]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
     -1 1 2 3 3 4 4 5
        |
               pointer
        Time O(n) and Space O(1)
        """
        cur = ListNode(-101)
        cur.next = head
        unique = cur
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val: 
                    head = head.next
                unique.next = head.next
            else:
                unique = unique.next
            head = head.next
        return cur.next
            
            