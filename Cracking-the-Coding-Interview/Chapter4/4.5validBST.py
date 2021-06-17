"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(root, minimum, maximum):
            if not root: return True
            if root.val <= minimum or root.val >= maximum: 
                return False
            return validate(root.left, minimum, root.val) and validate(root.right, root.val, maximum)
        return validate(root, minimum=float('-inf'), maximum=float('inf'))