# Definition for a binary tree node.
# Solution one Recursive Function

# DFS Binary Search ashiglan bodno
class TreeNode:
    # Ene heseg deer initialize hiij ogch baina
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # Ene recursive call hiigdej bodogdoh bogood edge case ni hervee root ni utga baihgui tohioldold root ni False baina 
    def hasPathSum(self, root, sum):
        if not root:
            return False
        
        # Val garj ireh bolgond sum aasaa hasaj ogoh bogood hervee sum ni hasagdsaar baigaad 0 tei tentseh uyd True butsaah yostoi
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
# Test Cases
root = TreeNode(5) 
root.left = TreeNode(4) 
root.right = TreeNode(8) 
root.left.left = TreeNode(11) 
root.left.left.left = TreeNode(7)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

calling = Solution()
print(calling.hasPathSum(root, 22))

# Complexity Analysis

# Time complexity : we visit each node exactly once, thus the time complexity is \mathcal{O}(N)O(N), where NN is the number of nodes.
# Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only one child node, the recursion call would occur NN times (the height of the tree), therefore the storage to keep the call stack would be \mathcal{O}(N)O(N). But in the best case (the tree is completely balanced), the height of the tree would be \log(N)log(N). Therefore, the space complexity in this case would be \mathcal{O}(\log(N))O(log(N)).





