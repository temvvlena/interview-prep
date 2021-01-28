# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ### Both Time and Space ON
        # if root is None: return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        """
           5
         /    \
        3      8
       / \    / \
      1   4  7   10
       [5 3 1]
        """
        stack, res = [], []
        curr = root
        if root is None: return res
        while curr is not None or len(stack) != 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
                
            
            