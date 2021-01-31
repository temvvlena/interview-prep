"""
https://leetcode.com/problems/binary-tree-right-side-view/
Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
  Time Complexity O(N) and Space O(D)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
           \
            7
            [1, 3, 4, 7]
            q[2, 3]
        """
        if root is None: return []
        q = deque([root])
        res = []
        while q:
            rightSide = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:res.append(rightSide.val)
        return res

        """
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
e = TreeNode(4)
f = TreeNode(7)
a.left = b
a.right = c
b.right = d
c.right = e
d.right = f
print(TreeNode.rightSideView(a,a))
        """