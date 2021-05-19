"""
Convert Sorted Array to Binary Search Tree
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Get the middle and then recurse
"""
# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
def sortedArrayToBST(nums):
    def helper(l, r, nums):
        if l > r: return None
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = helper(l, mid-1, nums)
        root.right = helper(mid+1, r, nums)
        return root
    return helper(0, len(nums)-1, nums)
    
    
