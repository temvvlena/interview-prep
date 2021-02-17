"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/
637. Average of Levels in Binary Tree
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Time Complexity O(n)
Space Complexity O(n)
"""
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        q = deque()
        q.append(root)
        res = []
        while q:
            qLength, val = len(q), 0
            for i in range(qLength):
                temp = q.popleft()
                val += temp.val
                if temp.left: q.append(temp.left)
                if temp.right: q.append(temp.right)
            res.append(val/qLength)
        return res            