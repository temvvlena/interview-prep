"""
https://leetcode.com/problems/random-pick-with-weight/
528. Random Pick with Weight
"""
import random


class Solution:
    def __init__(self, w: List[int]):
        self.presum = []
        total = 0
        for num in w:
            total += num
            self.presum.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.random() * self.total
        left, right = 0, len(self.presum)
        while left < right:
            mid = (right + left) // 2
            if self.presum[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    # Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
