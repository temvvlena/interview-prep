"""
https://leetcode.com/problems/symmetric-tree/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time and Space Complexity O(N)
class Solution:
    def isSymmetric(self, root):
        def _symmetric(n1, n2):        
            if not n1 and not n2: return True
            if  not n1 or not n2: return False
            return n1.val == n2.val and _symmetric(n1.left, n2.right) and _symmetric(n1.right, n2.left)
        return _symmetric(root, root)
"""
If the tree is empty, then it is symmetrical to the vertical 
axis going through its root node.

Else, check if the value at the root node of both subtrees 
is the same.

If it is, then check if the left subtree and the right 
subtree are symmetrical.

This can be done by checking if:

4.1 The root nodes of both trees contain the 
same value.

4.2 The left subtree of the left subtree and the 
right subtree of the right subtree are symmetrical.

4.3 The right subtree of the left subtree and the 
left subtree of the right subtree are symmetrical.
"""