"""
https://leetcode.com/problems/consecutive-characters/
Consecutive Characters
"""


class Solution:
    def maxPower(self, s: str) -> int:
        """
        abbbcccddddeeeeee
         ^
            ^
        aaaaa
        """
        max_count = 0
        count = 0
        prev = None

        if len(s) == 1: return 1

        for char in s:
            if char == prev:
                count += 1
            else:
                prev = char
                count = 1
            max_count = max(max_count, count)
        return max_count
