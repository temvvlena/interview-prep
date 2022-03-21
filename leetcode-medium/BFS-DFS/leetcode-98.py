"""
https://leetcode.com/problems/validate-binary-search-tree/
Validate Binary Search Tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        stack, prev = [], -2**32
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            val = root.val
            if val <= prev: return False
            prev = val
            root = root.right
        return True
