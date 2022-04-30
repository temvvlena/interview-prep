"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
215. Kth Largest Element in an Array
"""
from heapq import heappop, heapify


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        out = [-num for num in nums]
        heapify(out)
        for i in range(k - 1):
            heappop(out)
        return -out[0]
