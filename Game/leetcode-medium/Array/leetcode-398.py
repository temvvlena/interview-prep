"""
https://leetcode.com/problems/random-pick-index/
398. Random Pick Index
"""


class Solution:
    def __init__(self, nums: List[int]):
        self.dict = {}
        for index in range(len(nums)):
            if nums[index] not in self.dict:
                self.dict[nums[index]] = [index]
            else:
                self.dict[nums[index]].append(index)

    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
