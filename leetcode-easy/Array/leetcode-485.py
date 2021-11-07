"""
https://leetcode.com/problems/max-consecutive-ones/
Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

# Time and Space is O(N). Bruto Force Solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 1: return 1
            else: return 0
        myList = list()
        count = 1
        counter = 0 
        for i in nums:
            if i == 1: counter += 1
        if counter == 0: return 0
        
        for i in range(1, len(nums)):
            if nums[i] != 1:
                myList.append(count)
                count = 0 
            elif len(nums) == 2 and nums[1] == 1 and nums[0] == 0:
                myList.append(count)
                return max(myList)
            else:
                count += 1
                i += 1
        myList.append(count)
        return max(myList)