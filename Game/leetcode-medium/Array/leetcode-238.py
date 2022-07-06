"""
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
"""

class Solution:
    def productExceptSelf(self, nums):
        
        # Multiply the list from both sides: left and right
        # Then multiply them again
        # Time and Space complexity O(n)--linear

        # [ 1, 1, 2, 6]
        # [24, 12, 4, 1]
        length = len(nums)
        L, R, ans = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i-1] * L[i-1]
        R[-1] = 1
        for i in reversed(range(length-1)):
            R[i] = nums[i+1] * R[i+1]
        for i in range(length):
            ans[i] = L[i] * R[i]
        return ans
        