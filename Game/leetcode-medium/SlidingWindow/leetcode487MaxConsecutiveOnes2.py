"""
https://leetcode.com/problems/max-consecutive-ones-ii/
Max Consecutive Ones II

Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        1,0,1,1,0, 1, 1, 1
                ^
          ^
        """
        max_num = 0 
        slow = 0
        counter = 0 
        for fast in range(len(nums)):
            if nums[fast] == 0:
                counter += 1
            while counter == 2:
                if nums[slow] == 0:
                    counter -= 1
                slow += 1
            max_num = max(max_num, fast-slow+1)
        return max_num
                
            