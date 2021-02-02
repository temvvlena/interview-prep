"""
https://leetcode.com/problems/repeated-substring-pattern/
Repeated Substring Pattern
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
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
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Repeated pattern string looks like PatternPattern, and the others like Pattern1Pattern2.

        Let's double the input string:

        PatternPattern --> PatternPatternPatternPattern

        Pattern1Pattern2 --> Pattern1Pattern2Pattern1Pattern2

        Now let's cut the first and the last characters in the doubled string:

        PatternPattern --> *atternPatternPatternPatter*

        Pattern1Pattern2 --> *attern1Pattern2Pattern1Pattern*

        It's quite evident that if the new string contains the input string, the input string is a repeated pattern string.
        
        abababab
        
        Time is O(N Squared) and Space O(N)
        
        """
        return s in (s+s)[1:-1]
    
        