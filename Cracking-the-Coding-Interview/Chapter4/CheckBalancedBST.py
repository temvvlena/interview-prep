"""
Given a binary tree, determine if it is height-balanced.
    3
   / \
  9   20
      / \
     15  7   ---> True
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.balanced = True
    def validate(self, root):
        if not root: return True
        def helper(root):
            if root is None: return 0
            left = helper(root.left)
            right = helper(root.right)
            if abs(left-right)>1: 
                self.balanced = False
            return max(left, right)+1
        helper(root)
        return self.balanced

a = TreeNode(1)

b = TreeNode(2)
c = TreeNode(2)


d = TreeNode(3)
e = TreeNode(3)

f = TreeNode(4)
i = TreeNode(4)


a.left = b
a.right = c

b.left = d
b.right = e

d.right = f
d.left = i

print(Solution.validate(a, a))