"""
Given the root of a binary tree, 
return its maximum depth.

A binary tree's maximum depth is 
the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1

"""
Time complexity : we visit each node exactly once, thus the time complexity is 
O(N), where NN is the number of nodes.

Space complexity : in the worst case, the tree is completely unbalanced, 
e.g. each node has only left child node, the recursion call would occur NN times (the height of the tree), 
therefore the storage to keep the call stack would be O(N). 
But in the best case (the tree is completely balanced), 
the height of the tree would be log(N). 
Therefore, the space complexity in this case would be O(log(N)).
"""