"""
33. Search in Rotated Sorted Array
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Input: nums = [1], target = 0
Output: -1
"""
class Solution:
    def search(self, nums, target):
        # Brute Force Solution got TimeOut Error. 
        # O(n) is bad, so I should use Binary Search Algorithm O(logn)
        """
        if target in nums:
            return nums[target]
        else:
            return -1
        """
        # https://www.youtube.com/watch?v=U8XENwh8Oy8&ab_channel=NEETcode Learned from this
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            # This is the left side
            if nums[mid] >= nums[left]:
                if nums[mid] < target or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            # This is the right side
            else:
                if target < nums[mid] or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
        # Time (Log N) Space (1)
                    

        