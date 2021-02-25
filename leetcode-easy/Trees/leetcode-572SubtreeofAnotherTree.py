"""
https://leetcode.com/problems/subtree-of-another-tree/
Subtree of Another Tree
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time compexity N^2 and Space max(m,n)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        if string_t in string_s: return True
        return False
    def traverse_tree(self, s):
        if s is None: return None
        return f"*{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        """
        if t is None and s is None: return True
        if s is not None and t is None: return False
        if s is None and t is not None: return False
        if s.val != t.val: return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return self.isSubtree(s.left, t.left) and self.isSubtree(s.right, t.right) and s.val == t.val
        """