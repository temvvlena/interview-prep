"""
https://leetcode.com/problems/assign-cookies/
455. Assign Cookies
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g:
            return 0
        result = 0
        g.sort()
        s.sort()
        index1 = 0
        index2 = 0
        """
        7 8 9 10 k
        ^
        5 6 7 8 c
            ^
        """
        while index1 < len(g) and index2 < len(s):
            if g[index1] <= s[index2]:
                result += 1
                index1 += 1
                index2 += 1
            else:
                index2 += 1
        return result
