"""
Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree 
of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of 
this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None: return True
        if s is None: return False
        if s.val == t.val:
            if self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def is_same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None: return True
        elif s is None or t is None: return False
        if s.val == t.val: return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)
        """
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        if string_t in string_s: return True
        return False
    def traverse_tree(self, s):
        if s is None: return None
        return f"*{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        """