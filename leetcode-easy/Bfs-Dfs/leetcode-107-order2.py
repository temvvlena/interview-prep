"""
107. Binary Tree Level Order Traversal II
Add to List
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time O(N)
# Space O(N)
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = deque() 
        q.append(root)
        res = []
        while q:
            qLength = len(q)
            temp = []
            for i in range(qLength):
                current = q.popleft()
                temp.append(current.val)
                if current.left: q.append(current.left)
                if current.right: q.append(current.right)
            res.append(temp)
        return res[::-1]