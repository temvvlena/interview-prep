"""
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
Longest Substring with At Most K Distinct Characters
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n *k==0: return 0
        
        left = 0
        maximum = 1
        sHash = {}
        for right in range(len(s)):
            character = s[right]
            sHash[character] = right
            right += 1
            if len(sHash) == k+1:
                # delete the items
                # update left += 1
                minimum = min(sHash.values())
                del sHash[s[minimum]]
                left = minimum + 1
            maximum = max(maximum, right-left)

        return maximum
        
        """
        n = len(s)
        if n *k==0: return 0
        
        left, right = 0, 0
        maximum = 1
        sHash = {}
        
        while right < n:
            character = s[right]
            sHash[character] = right
            right += 1
            
            if len(sHash) == k+1:
                # delete the items
                # update left += 1
                minimum = min(sHash.values())
                del sHash[s[minimum]]
                left = minimum + 1
            
            maximum = max(maximum, right-left)
            
        return maximum
        """