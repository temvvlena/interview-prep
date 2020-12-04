class Solution:
    def maxSubArray(self, nums) -> int:
        # This is Kadane's Algorithm. O(n) Linear
        max_global, max_current = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], nums[i] + max_current)
            if max_current > max_global:
                max_global = max_current
        return max_global
        

#Follow up: If you have figured out the O(n) solution, 
#try coding another solution using the divide and conquer approach, which is more subtle.

# Have not finished this part yet. I will update that tomorrow. 
# Divide and Conquer Algorithm
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, low, high):
        if low > high:
            return 0
        if low == high:
            return nums[low]
        mid = low + (high-low)//2
        x_left = self.helper(nums, low, mid)
        x_right = self.helper(nums, mid+1, high)
        lmax, rmax = float('-inf'), float('-inf')
        lsum, rsum = 0,0
        for i in range(mid-1, low-1, -1): ### Important Insight in NlgN solutions
            lsum = lsum + nums[i]
            lmax = max(lmax, lsum)
        for i in range(mid+1, high+1, 1):
            rsum = rsum + nums[i]
            rmax = max(rmax, rsum)
        return max(x_left, x_right, max(0,lmax)+max(0,rmax)+nums[mid]) 
"""  