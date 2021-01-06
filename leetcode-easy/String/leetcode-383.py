"""
https://leetcode.com/problems/ransom-note/solution/
Given an arbitrary ransom note string and another string containing letters 
from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstruct(self, ransomNote, magazine):
        # One HashMap is better that using two
        # Time Complexity will be O(M) because if ransomNote is greater than magazine, 
        # It will be False. Space Complexity will be constant because K can't be more than unique 26 char
        if len(ransomNote) > len(magazine): return False
        h1 = {}
        for i in range(len(magazine)):
            if magazine[i] not in h1: h1[magazine[i]] = 1
            else: h1[magazine[i]] += 1
        print(h1)
        for c in ransomNote:
            if c not in h1: return False
            elif h1[c] <= 0: return False
            h1[c] -= 1
        return True
    """
        # Using two HashMaps
        if len(ransomNote) > len(magazine): return False
        h1 = {}
        h2 = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] not in h1: h1[ransomNote[i]] = 1
            else: h1[ransomNote[i]] += 1
        for i in range(len(magazine)):
            if magazine[i] not in h2: h2[magazine[i]] = 1
            else: h2[magazine[i]] += 1
        for aKey in h1.keys():
            if aKey not in h2: return False
            if h1[aKey] > h2[aKey]: return False
        return True
    """        
                
        
        