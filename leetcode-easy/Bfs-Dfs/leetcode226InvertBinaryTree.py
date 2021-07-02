from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if root is not None: root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root
        if root is None: return None
        q= deque()
        q.append(root)
        while q:
            current = q.popleft()
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left != None: 
                q.append(current.left)
            if current.right != None:
                q.append(current.right)
        return root