"https://leetcode.com/problems/implement-strstr/"
# Time and Space O(1)
class Solution:
    def strStr(self, haystack: str, needle: str):
        if needle in haystack: return haystack.index(needle)
        else: return -1