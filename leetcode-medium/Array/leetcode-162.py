"""
https://leetcode.com/problems/find-peak-element/
162. Find Peak Element
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(N) Algorithm --> return nums.index(max(nums))
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
