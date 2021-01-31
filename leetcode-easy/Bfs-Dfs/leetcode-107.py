"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]: 
        """
            3
           / \
          9  20
         /   /  \
        8   15   7
        
          [9, 20], 
          [3], [9, 20]
          
          [[3], [9,20],[15,7]]
        
        """
        pass
        #DFS
        
        
        """
        BFS
        if root is None: return []
        res = []
        q = deque([root])
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(temp)
        return res[::-1]
        """
        
            
            
