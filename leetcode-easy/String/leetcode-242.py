"""
https://leetcode.com/problems/valid-anagram/
Check Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s, t):
        # Time is O(N) and Space is O(1) because Although we do use extra space, 
        # the space complexity is O(1) because the table's size 
        # stays constant no matter how large n is.
        myHash = {}
        if len(s) != len(t): return False
        for i in s:
            if i not in myHash: myHash[i] = 1
            else: myHash[i] += 1
        for i in t:
            if i in myHash: myHash[i] -= 1
        for i in myHash:
            if myHash[i] >= 1: return False
        return True
        # One can also use Sorted. But that will give Time Complexity NLogN and space O(1)