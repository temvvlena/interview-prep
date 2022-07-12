"""
https://leetcode.com/problems/simplify-path/
71. Simplify Path
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for char in path.split("/"):
            if char == "." or char == "":
                continue
            if char == "..":
                if res:
                    res.pop()
            else:
                res.append(char)
        out = "/" + "/".join(res)
        return out
