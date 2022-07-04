"""
https://leetcode.com/problems/closest-binary-search-tree-value/
270. Closest Binary Search Tree Value
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        q = deque([root])
        res = []
        while q:
            for i in range(len(q)):
                temp = q.popleft()
                res.append([temp.val, abs(target - temp.val)])
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        res.sort(key=lambda x: x[1])
        return res[0][0]


"""
import math
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def preorder(root):
            if not root:
                return []
            else:
                res.append([root.val, abs(target-root.val)])
                preorder(root.left)
                preorder(root.right)
        res = []
        preorder(root)
        res.sort(key=lambda x: x[1])
        return res[0][0]
"""
