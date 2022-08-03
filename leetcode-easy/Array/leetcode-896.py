"""
https://leetcode.com/problems/monotonic-array/submissions/
896. Monotonic Array
"""


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        increasing = decreasing = True
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                increasing = False
            if nums[index] < nums[index + 1]:
                decreasing = False
        return increasing or decreasing
        """
        def increasing():
            slow = 0
            for fast in range(1, len(nums)):
                if nums[fast] < nums[slow]:
                    return False
                slow += 1
            return True

        def decreasing():
            slow = 0 
            for fast in range(1, len(nums)):
                if nums[fast] > nums[slow]:
                    return False
                slow += 1
            return True

        if len(nums) == 1:
            return True

        i = 0 
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                break
            i += 1

        answer = increasing() if nums[i] < nums[j] else decreasing()
        return answer
        """
