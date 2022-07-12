"""
https://leetcode.com/problems/top-k-frequent-elements/
Top K Frequent Elements
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHash = Counter(nums)
        res = [[aKey, aValue] for aKey, aValue in myHash.items()]
        res.sort(key=lambda x: x[1], reverse=True)
        out = []
        for i in range(k):
            out.append(res[i][0])
        return out
