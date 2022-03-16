"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        #1 -> 2 -> 3
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else: current = current.next
        return head
        """
        Again tried to solve in 2022 March. Failed at first.
        if not head: return head
        cur = head
        while cur and cur.next:
            temp = cur.next
            while temp and temp.val == cur.val:
                temp = temp.next
            cur.next = temp
            cur = cur.next
        return head
        """
        """
        # Solved in April
        if not head: return head
        cur = head
        while cur and cur.next:
            temp = cur.next
            while temp and cur.val == temp.val:
                temp = temp.next     
            cur.next = temp
            cur = cur.next
        return head
        
        # Solved in January
        curr = head
        if head is None: return 
        while curr.next:
            if curr.val == curr.next.val and curr.next != None:
                newValue = curr.next.next
                curr.next = newValue
            else: curr = curr.next
        return head
        """