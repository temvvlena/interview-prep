"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
236. Lowest Common Ancestor of a Binary Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        if root == None or root == p or root == q:
            return root

        # Find p/q in left subtree
        l = self.lowestCommonAncestor(root.left, p, q)

        # Find p/q in right subtree
        r = self.lowestCommonAncestor(root.right, p, q)

        # If p and q found in left and right subtree of this node, then this node is LCA
        if l and r:
            return root

        # Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
        return l if l else r

    def lowestCommonAncestorDFS(self, root, p, q):

        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans

    def lowestCommonAncestorBST(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = res.pop()
            if node.left:
                parent[node.left] = node
                res.append(node.left)
            if node.right:
                parent[node.right] = node
                res.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
