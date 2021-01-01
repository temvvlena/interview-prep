"""
https://leetcode.com/problems/repeated-substring-pattern/
Given a non-empty string check if it can be constructed 
by taking a substring of it and appending multiple copies 
of the substring together. You may assume the given string 
consists of lowercase English letters only and its length 
will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.
"""
class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)
        dp = [0] * n
        # Construct partial match table (lookup table).
        # It stores the length of the proper prefix that is also a proper suffix.
        # ex. ababa --> [0, 0, 1, 2, 1]
        # ab --> the length of common prefix / suffix = 0
        # aba --> the length of common prefix / suffix = 1
        # abab --> the length of common prefix / suffix = 2
        # ababa --> the length of common prefix / suffix = 1
        for i in range(1, n):
            j = dp[i - 1]
            while j > 0 and s[i] != s[j]:
                j = dp[j - 1]
            if s[i] == s[j]:
                j += 1
            dp[i] = j

        l = dp[n - 1]
        # check if it's repeated pattern string
        return l != 0 and n % (n - l) == 0