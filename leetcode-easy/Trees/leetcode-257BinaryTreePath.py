"""
https://leetcode.com/problems/binary-tree-paths/
Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.
Example:
Input:
   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None: 
                paths.append(path)
            if node.left: 
                stack.append((node.left, path+'->'+str(node.left.val)))
            if node.right: 
                stack.append((node.right, path+'->'+str(node.right.val)))
        return paths        
        
        """
        if root is None: return []
        res = ""
        output = []
        def helper(root, res):
            if root:
                if res == "": res = str(root.val)
                else: res = res + "->" + str(root.val)
            if root.left is not None:
                helper(root.left, res)
            if root.right is not None:
                helper(root.right, res)
            if root.right is None and root.left is None:
                output.append(res)
        helper(root, res)
        return output
        """