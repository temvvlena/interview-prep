"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
1047. Remove All Adjacent Duplicates In String
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for char in s:
            if not res:
                res.append(char)
            elif res[-1] == char:
                res.pop()
            else:
                res.append(char)
        return "".join(res)
