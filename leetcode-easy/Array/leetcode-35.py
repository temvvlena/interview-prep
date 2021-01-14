"""
https://leetcode.com/problems/search-insert-position/
Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        Time Complexity: Log(N)
        Space Complexity: O(1)
        """
        low, high, pos = 0, len(nums) -1, 0
        while low <= high:   
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            elif target > nums[mid]: 
                low = mid + 1
                pos = mid + 1
            else:
                high = mid - 1
                pos = mid
        return pos
        