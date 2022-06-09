"""
https://leetcode.com/problems/permutation-in-string/
Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Constraints:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
Time O(Lengof s1 + length of s2)
Space O(1)
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1_counter = Counter(s1)
        s2_counter = Counter()
        length_s1 = len(s1)
        for count, value in enumerate(s2):
            s2_counter[value] += 1
            if count >= length_s1:
                leftest_element = s2[count - length_s1]
                if s2_counter[leftest_element] == 1:
                    del s2_counter[leftest_element]
                else:
                    s2_counter[leftest_element] -= 1
            if s2_counter == s1_counter:
                return True
        return False
