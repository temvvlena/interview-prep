"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
215. Kth Largest Element in an Array
"""
from heapq import heappop, heapify


# Time complexity : O(Nlogk).
# Space complexity : O(K) to store the heap elements
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        out = [-num for num in nums]
        heapify(out)
        for i in range(k - 1):
            heappop(out)
        return -out[0]

    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        for index in range(len(nums) - 1, -1, -1):
            if i == k - 1:
                return nums[index]
            k -= 1
    """
