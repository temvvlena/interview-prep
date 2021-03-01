"""
https://leetcode.com/problems/sum-of-left-leaves/solution/
Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.
Example:

    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:  
        def helper(root, is_leaf):
            if not root: return 0
            if root.left is None and root.right is None:
                if is_leaf:
                    return root.val
                else: 0
            return helper(root.left, True)+helper(root.right, False)     
        return helper(root, is_leaf = False)
        """
        Iterative
        Space and Time will be O(N)
        if not root: return 0
        def is_leaf(node): if node is not None and node.left is None and node.right is None: return True
        q = deque()
        q.append(root)
        res = 0
        while q:
            cur = q.popleft()
            # if cur.left exists and cur.left is a leaf node
            if is_leaf(cur.left): res += cur.left.val 
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        return res
        """