"""
https://leetcode.com/problems/range-sum-query-immutable/
303. Range Sum Query - Immutable
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.cashing = self.cashingPairs(nums, left=0, right=len(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.cashing[right] - self.cashing[left - 1]

    def cashingPairs(self, nums, left, right):
        myHash = {-1: 0}
        for i in range(left, right): myHash[i] = myHash[i - 1] + nums[i]
        return myHash


# Approach 2 --> Time limit Exceed
class NumArray:

    def __init__(self, nums: List[int]):
        self.myArray = nums

    def sumRange(self, left: int, right: int) -> int:
        ans = 0
        while left <= right:
            ans += self.myArray[left]
            left += 1
        return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
