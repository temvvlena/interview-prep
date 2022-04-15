"""
https://leetcode.com/problems/longest-common-prefix/
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        res = []
        for i in range(len(min(strs))):
            for j in range(1, len(strs)):
                if strs[0][i]==strs[j][i]:
                    if j==len(strs)-1:
                        res.append(strs[0][i])
                else:
                    return "".join(res)
        return "".join(res)
