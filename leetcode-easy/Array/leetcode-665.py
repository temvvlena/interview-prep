"""
Non-decreasing Array
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if self.tryFix(nums): return True
        return self.tryFix(nums[::-1], lambda n,p: p<n)
    def tryFix(self, nums: List[int], predict=lambda n,p: n<p) -> bool:
        prev = nums[0]
        fixed = False
        for n in nums:
            if predict(n, prev):
                if fixed: return False
                fixed = True
            else: prev = n
        return True
    
    
    """
    Solution 2
    p = None
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            if p is not None: return False
            p = i
    return (p is None or p == 0 or p == len(nums) - 2 or nums[p] <= nums[p+2] or nums[p+1] >= nums[p-1])
    """
