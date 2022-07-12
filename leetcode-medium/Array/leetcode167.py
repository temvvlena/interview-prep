"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Two Sum II - Input Array Is Sorted
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers) - 1
        while first <= last:
            temp = numbers[first] + numbers[last]
            if temp == target:
                return [first + 1, last + 1]
            elif temp > target:
                last -= 1
            else:
                first += 1
