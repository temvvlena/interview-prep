"""
https://leetcode.com/problems/partition-list/
Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        So, I have to move all the elements if 
        
        1 -> 4 -> 3 -> 2 -> 5 -> 2
                  |
                                 ^
        Before
        1 -> 2 -> 2 -> None
        After
        4 -> 3 -> 5 -> None
        1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None
        
        """
        before = before_head = ListNode(-1)
        after = after_head =  ListNode(-1)
        while head:
            if x > head.val:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next