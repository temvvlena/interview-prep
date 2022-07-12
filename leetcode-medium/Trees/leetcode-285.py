"""
Inorder Successor in BST
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.
Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
Note:
If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """
        [[5,3,6,2,4,null,null,1]]
        """
        if root.left is None and root.right is None: return None
        stack = [root]
        found = False
        while stack:
            cur = stack[-1]
            while cur.left:
                res = cur
                stack.append(cur.left)
                cur = cur.left
                res.left = None
            temp = stack.pop()
            if found is True:
                return temp
            if temp.val == p.val: 
                found = True
            if temp.right:
                stack.append(temp.right)
        return None
    """
    O(N)
    def __init__(self):
        self.found = False
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root.left is None and root.right is None: return None
        res = []
        def helper(myTree):
            if not myTree:
                return 
            helper(myTree.left)
            if self.found is True:
                res.append(myTree)
                return
            if myTree.val == p.val: 
                self.found = True
            helper(myTree.right)
        helper(root)
        if len(res) != 0:
            return res[0]
        return None
        # Solution 3
        def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
            res = None
            while root:
                if root.val > p.val: res, root = root, root.left
                else: root = root.right
            return res
        """
