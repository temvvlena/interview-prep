"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/
Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        pHash = Counter(p)
        sHash = Counter()
        res = []
        for i in range(len(s)):
            sHash[s[i]]+=1
            if i >= len(p):
                # have to check two cases
                # delete if equal to 1
                # reduce -1
                if sHash[s[i-len(p)]] == 1:
                    del sHash[s[i-len(p)]]
                else:
                    sHash[s[i-len(p)]] -= 1
            if sHash == pHash:
                res.append(i-len(p)+1)
        return res