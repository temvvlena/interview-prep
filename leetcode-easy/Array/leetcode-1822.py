"""
https://leetcode.com/problems/sign-of-the-product-of-an-array/
1822
"""


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        output = nums[0]
        for i in range(1, len(nums)):
            output *= nums[i]
        if output > 1:
            return 1
        elif output <= -1:
            return -1
        else:
            return 0
