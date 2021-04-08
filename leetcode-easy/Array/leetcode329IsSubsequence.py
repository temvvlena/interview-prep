"""
https://leetcode.com/problems/is-subsequence/
Is Subsequence
Given two strings s and t, check if s is a subsequence of t.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0: return True
        left = 0
        i = 0 
        while i <= len(t)-1 and left <= len(s)-1:
            if t[i] == s[left]:
                left += 1
            i += 1
        return left == len(s)