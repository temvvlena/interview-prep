# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.res = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if root:
            self.helper(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return 
            self.helper(root.right) 
        """
        stack = []
        cur = root
        while cur is not None or len(stack)>0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            k -= 1
            if k == 0 :
                return temp.val
            cur = temp.right
    def kthSmallest-1(self, root: TreeNode, k: int) -> int:
        stack = []
        res = []
        cur = root
        while cur is not None or len(stack)>0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            res.append(temp.val)
            cur = temp.right
        return res[k-1]    
    def kthSmallest-2(self, root: TreeNode, k: int) -> int:
        def helper(myTree):
            if not myTree: return []
            return helper(myTree.left)+[myTree.val]+helper(myTree.right)
        
        myList = helper(root)
        return myList[k-1]
        """