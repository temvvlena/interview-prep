"""
https://leetcode.com/problems/invert-binary-tree/
Invert a binary tree.
Example:
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

class Solution:
    def invertTree(self, root):
        if root != None: root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root