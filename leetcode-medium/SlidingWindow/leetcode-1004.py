"""
https://leetcode.com/problems/max-consecutive-ones-iii/
1004. Max Consecutive Ones III
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
         0 1 2 3 4 5 6 7 8 9 10
        [1,1,1,0,0,0,1,1,1,1,0], k = 2
         ^
                 ^
        THIS QUESTION IS HARD AF!!!!
        """
        maxLength = 0
        left = 0
        second = 0
        counter = 0
        while second < len(nums):
            if nums[second] == 0:
                counter += 1
            while counter > k:
                if nums[left] == 0:
                    counter -= 1
                left += 1
            maxLength = max(maxLength, second - left + 1)
            second += 1
        return maxLength
