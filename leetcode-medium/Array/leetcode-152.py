"""
Given an integer array nums, 
find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

Example 1)
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2)
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums):
        # Same as Kadane's Algorithm
        # Have to think about minValue when multiplying

        # First as the same as Kadane's algorithm, set the first values
        minValue, maxValue, maxAnswer = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            # store the maxValue, cuz we are updating it but need to use for minVAlue
            temp = maxValue
            maxValue = max(nums[i], maxValue*nums[i], minValue*nums[i])
            minValue = min(nums[i], temp*nums[i], minValue*nums[i])
            maxAnswer = max(maxValue, maxAnswer)
            # if maxValue > maxAnswer:
            #   return maxAnswer = maxValue
        return maxAnswer

        # Time complexity O(n) & Space complexity is O(1) cuz we are using 3 variables

        # Brute Force Solution would be multiplying all the subarrays and then find the max. 
        # However, this approach will be time-consuming. O(n^2)

        # While doing some other research found another solution that I found quite interesting
        # it's basically updating the list from right and left. Then returning the max solution. 
        # it's kinda similar to Leetcode 238
"""
        muns = nums[::-1]
        for i in range(1, len(nums)):            
            if nums[i-1] != 0:
                nums[i] *= nums[i-1]
                
            if muns[i-1] != 0:
                muns[i] *= muns[i-1]
                
        return max(nums + muns)
"""