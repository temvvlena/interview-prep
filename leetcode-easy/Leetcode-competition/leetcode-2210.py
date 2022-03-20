"""
https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
"""
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        """
        [2, 4, 6, 8, 11, 4, 1, 1, 6, 5]
        """
        count, last = 0, nums[0]
        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1]:
                last = nums[i-1]
            else:
                last
            if last < nums[i] > nums[i+1] or last > nums[i] < nums[i+1]:
                count += 1
        return count