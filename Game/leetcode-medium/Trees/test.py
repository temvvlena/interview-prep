"""
Inorder -> SC630
Postorder -> S603C
Preorder -> CS360

myList = [C, ]

reverse postoder
C306S

Inorder -> S630
Postorder -> S603

306S


        C
      /   \
     S     3
          /  \
         6    0   


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_preorder(inorder, postorder):
    """Return pre-order traversal of a tree based on its in-order and post-order traversals"""
    
    def rec(inorder, postorder):
        if not inorder or not postorder:
            return
        # This will be always the node
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)

        root.right = rec(inorder[mid+1:], postorder)
        root.left = rec(inorder[:mid], postorder)
        return root
    return ( rec(inorder, postorder) )

print(get_preorder(['S', 'C', '6','3','0'], ["S", "6", "0", "3", "C"]))