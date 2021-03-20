"""
https://leetcode.com/problems/max-consecutive-ones/
Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Time O(N) and Space O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = 0
        max_count = 0
        for i in nums:
            if i == 1: temp += 1
            else: 
                max_count = max(max_count, temp)
                temp = 0
        return max(max_count, temp)   
