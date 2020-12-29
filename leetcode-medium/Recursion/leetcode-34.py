# https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        firstVal = head
        secondVal = head.next
        
        firstVal.next = self.swapPairs(secondVal.next)
        secondVal.next = firstVal
        
        return secondVal
"""
head = [1,2,3,4,Null]
Once it reaches Null, it swaps 4, 3, then 2, 1
Time and Space Complexity O(N)

"""