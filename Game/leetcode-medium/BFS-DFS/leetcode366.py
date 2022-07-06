"""
https://leetcode.com/problems/find-leaves-of-binary-tree/submissions/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = collections.defaultdict(list)
        def dfs(root):
            leftHeight, rightHeight = 0, 0

            if root.left is None and root.right is None:
                res[0].append(root.val)
                return 0

            if root.left:
                leftHeight = dfs(root.left)

            if root.right:
                rightHeight = dfs(root.right)

            new_height = 1+max(leftHeight, rightHeight)
            res[new_height].append(root.val)
            return new_height
        dfs(root)
        return res.values()
