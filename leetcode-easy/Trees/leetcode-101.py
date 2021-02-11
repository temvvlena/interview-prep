# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        1 -> 2 -> 3
        1 -> 2 -> 4
        [1,2,2,null,3,null,3]
        3 case
        1 -- tentsuu
        2 -- zuun ni baruun
        3 -- baruun ni zuun
        
        def helper(root1, root2):
            if root1 is None and root2 is None: return True
            if root1 is None or root2 is None: return False
            if root1.val == root2.val: return helper(root1.left, root2.right) and helper(root1.right, root2.left)
            return False
        return helper(root, root)
        Time and Space O(N)
         """
        def helper(root1, root2):
            myStack = []
            myStack.append(root1)
            myStack.append(root2)
            while myStack != []:
                temp1 = myStack.pop()
                temp2 = myStack.pop()
                if temp1 is None and temp2 is None: continue
                if temp1 is None or temp2 is None: return False
                if temp1.val != temp2.val: return False
                myStack.append(temp1.left)
                myStack.append(temp2.right)
                myStack.append(temp1.right)
                myStack.append(temp2.left)
            return True
        return helper(root, root)
       
        
