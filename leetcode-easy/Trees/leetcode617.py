"""
https://leetcode.com/problems/merge-two-binary-trees/
Given two binary trees and imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree.
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1, t2):
        
        if t1 is None and t2 is None:
            return None
        
        if t1 is None:
            nT = TreeNode(t2.val)
            nT.left = self.mergeTrees(None, t2.left)
            nT.right = self.mergeTrees(None, t2.right)
            return nT
        
        if t2 is None:
            nT = TreeNode(t1.val)
            nT.left = self.mergeTrees(None, t1.left)
            nT.right = self.mergeTrees(None, t1.right)
            return nT
        
        newTree = TreeNode(t1.val + t2.val)
        newTree.left = self.mergeTrees(t1.left, t2.left)
        newTree.right = self.mergeTrees(t1.right, t2.right)     
        return newTree