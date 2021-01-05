"""
https://leetcode.com/problems/reverse-linked-list/
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""
class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        # print(head.next.next.val)
        head.next.next = head
        head.next = None
        return p
    # Both works     
    def reverseListAnother(self, head, prev=None):   
        if not head:
            return prev
        temp = head.next
        head.next = prev
        return self.reverseListAnother(temp, head)
