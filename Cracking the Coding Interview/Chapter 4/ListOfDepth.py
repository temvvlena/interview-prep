class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root): 
    # Return None. Modifies the list
    def helper(node):
        if node is None: return None
        if node.left is None and node.right is None: return node
        leftTail = helper(node.left)
        rightTail = helper(node.right)
        
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        if rightTail: return rightTail
        return leftTail
    helper(root)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

e = TreeNode(5)
f = TreeNode(6)

a.left = b
b.left = c
b.right = d

a.right = e
e.right = f

print(flatten(a))