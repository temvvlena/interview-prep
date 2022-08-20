"""
https://leetcode.com/problems/find-lucky-integer-in-an-array/
1394. Find Lucky Integer in an Array
"""
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        arr.sort(reverse=True)
        for num in arr:
            if num == freq[num]:
                return num
        return -1
