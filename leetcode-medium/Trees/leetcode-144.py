# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
          1
         / \
      None  2
           /  
          3 
        Pre-order --> root, left, right
        In- order --> left, root, right
        Post - order --> left, right, root
        # Recursively and Iterate
        
        3 1 2
       / \
      1   2
      O(N) Time and Space 
        """
        # if root is None: return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)   
        # stack = list()
        # res = list()
        # if root is None: return res
        # stack.append(root)
        # while len(stack) != 0:
        #     newNode = stack.pop()
        #     res.append(newNode.val)
        #     if newNode.right is not None: stack.append(newNode.right)
        #     if newNode.left is not None: stack.append(newNode.left) 
        # return res
        node, output = root, []
        while node:  
            if not node.left: 
                output.append(node.val)
                node = node.right 
            else: 
                predecessor = node.left 

                while predecessor.right and predecessor.right is not node: 
                    predecessor = predecessor.right 

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node  
                    node = node.left  
                else:
                    predecessor.right = None
                    node = node.right         

        return output