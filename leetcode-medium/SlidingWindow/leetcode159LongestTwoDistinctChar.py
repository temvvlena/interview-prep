"""
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/solution/
Longest Substring with At Most Two Distinct Characters
Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

Time O(N) and Space O(1)
"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        left = 0
        right = 0 
        sHash = {}
        maximum = 1
        """
        eceba
        ^
        {e:0, c: 1, }
        """
        for i in range(len(s)):
            sHash[s[i]] = i
            right += 1
            
            if len(sHash) == 3:
                # do all sorts of deletion
                minimum = min(sHash.values())
                del sHash[s[minimum]]
                left = minimum + 1
            
            maximum = max(maximum, right-left)
        
        return maximum