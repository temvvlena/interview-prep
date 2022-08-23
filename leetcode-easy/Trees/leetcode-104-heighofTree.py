"""
Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:
Input: root = [1,null,2]
Output: 2
Example 3:
Input: root = []
Output: 0
Example 4:
Input: root = [0]
Output: 1
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
104. Maximum Depth of Binary Tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # bfs solution
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1

        depth, level = 0, deque([root])
        while level:
            depth += 1
            for i in range(len(level)):
                node = level.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return depth


"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
        else:
            left_height = self.maxDepth(root.left)
            rigth_height = self.maxDepth(root.right)
            return max(left_height, rigth_height)+1
"""
