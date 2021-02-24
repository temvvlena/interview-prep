# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time O(N) and Space O(1)
class Solution:
    def __init__(self):
        self.a = TreeNode()
        self.cur = self.a
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if root is None: return
            helper(root.left)
            self.cur.right = root
            self.cur = self.cur.right
            self.cur.left = None
            helper(root.right)
        helper(root)
        self.cur.right = None
        return self.a.right    
        """
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        root.right
        Time and Space O(N)
        
        def helper(root):
            if root is None: 
                return []
            return helper(root.left) + [root] + helper(root.right)
        myList = helper(root)
        i = 0
        while i < len(myList)-1:
            myList[i].right = myList[i+1]
            myList[i].left = None
            i +=1
        myList[-1].right = None
        myList[-1].left = None
        return myList[0]
        """