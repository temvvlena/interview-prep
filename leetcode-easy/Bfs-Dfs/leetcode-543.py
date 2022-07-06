"""
https://leetcode.com/problems/diameter-of-binary-tree/
543. Diameter of Binary Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def h(node):
            nonlocal diameter
            if not node:
                return 0
            left = h(node.left)
            right = h(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        diameter = 0
        h(root)
        return diameter
