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
        