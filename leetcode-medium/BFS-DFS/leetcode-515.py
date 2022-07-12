"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""

import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque()
        q.append(root)
        res = []
        while q:
            max_number = -math.inf
            for i in range(len(q)):
                cur = q.popleft()
                if cur.val > max_number:
                    max_number = max(max_number, cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(max_number)
        return res
