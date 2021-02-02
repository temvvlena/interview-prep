"""
https://leetcode.com/problems/same-tree/
Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#from collections import deque
# Time is O(N) and Space O(N)
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q: return False
        if q is None and p: return False
        if q is None and p is None: return True
        if p.val != q.val: return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)  
        
        """
        if p is None and q: return False
        if q is None and p: return False
        if q is None and p is None: return True
        return self.preOrderTraversal(p) == self.preOrderTraversal(q)
    def preOrderTraversal(self, root):
        myList = []
        if root:
            myList.append([root.val])
            myList.append(self.preOrderTraversal(root.left))
            myList.append(self.preOrderTraversal(root.right))
        return myList
        """
        