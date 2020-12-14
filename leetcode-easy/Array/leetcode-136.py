"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""
# This can be solved multiple ways: hashing, set operator, and etc. But space complexity will be N 
# To make it (1), gotta use bitwise operation
def singleNumber( nums):
        """
        Only use linear time complexity and 0 space complexity
        :type nums: List[int]
        :rtype: int
        a ^ 0 = 0
        a ^ a = 0
        a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
        """
        a = 0
        for i in nums:
            a ^= i
        return a
print(singleNumber([1,1,2,3,2]))