"""
https://leetcode.com/problems/reverse-linked-list/submissions/
Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        1 2 3 4 5 -> None
           None
           
        1 2 3 4 5 -> None
        2 1     3 4 5
        3 2 1    4 5 
        4 3 2 1   5
        5 4 3 2 1  None
        Tail recursion (Read)
        """
        newNode = None
        def helper(newNode, head): 
            if head is None: 
                return newNode
            temp = head.next
            head.next = newNode
            return helper(head, temp)
        return helper(newNode, head)
    
    """
        previous = None
        while head:
            temp = head.next
            head.next = previous
            previous = head
            head = temp
        return previous
    

          Null<-1<-2<-3<-4<-5 -> Null
               |
        1 -> 2-> 3-> 4 -> 5 -> Null
        |
        
         """