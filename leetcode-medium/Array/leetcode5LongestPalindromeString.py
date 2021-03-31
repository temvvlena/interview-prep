"""
https://leetcode.com/problems/longest-palindromic-substring/
Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str: 
        def isPalindrome(s, left, right):
            while left<right:
                if s[left]!=s[right]: return False
                left += 1
                right -= 1
            return True
        left = 0 
        right = 1
        i = 1
        while i<len(s):
            k = right - left
            if (i-k-1>=0 and isPalindrome(s, i-k-1, i)):
                left = i-k-1
                right = i + 1
            else: 
                if isPalindrome(s, i-k, i):
                    left = i -k
                    right = i + 1
            i += 1
        return s[left:right]