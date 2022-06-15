"""
https://leetcode.com/problems/combinations/
Combinations
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, cur=[]):
            if len(cur) == k:
                output.append(cur[:])
            for i in range(first, n + 1):
                cur.append(i)
                backtrack(i + 1, cur)
                cur.pop()

        output = []
        backtrack()
        return output
