"""
https://leetcode.com/problems/balanced-binary-tree/
Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def __init__(self):
        self.balanced = True
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        def getHeight(myTree):
            if myTree is None: return 0
            left = getHeight(myTree.left)
            right = getHeight(myTree.right)
            if abs(left-right) > 1: self.balanced = False
            return max(left, right)+1
        check = getHeight(root)
        return self.balanced
