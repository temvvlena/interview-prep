"""
https://leetcode.com/problems/palindrome-linked-list/
Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None: return True
        s = head
        f = head
        prev = None
        
        while f != None and f.next != None: # 1 -> 2 -> 2 -> 3 -> 1
            f = f.next.next
            temp = s.next
            s.next = prev
            prev = s
            s = temp
            
        if f != None:
            s = s.next
            
        while prev != None and s != None:
            if prev.val != s.val: return False
            prev = prev.next
            s = s.next
            
        return True

        """
        myList = []
        while head is not None:
            myList.append(head.val)
            head = head.next
        return myList==myList[::-1]
        """


        """
        Solved on March 16, 2022
        s = head
        f = head
        cur = None
        while f is not None and f.next is not None:
            f = f.next.next # 2 -> 1
            temp = s.next # 2 -> 2 -> 1
            s.next = cur # 1 -> None
            cur = s # 1(pointer) -> None
            s = temp # 1 -> None  Odoo bolohoor  2 -> 2 -> 1
        if f is not None:
            s = s.next
        while s is not None:
            if s.val != cur.val: return False
            s = s.next
            cur = cur.next
        return True
        """
    