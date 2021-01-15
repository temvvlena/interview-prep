"""
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in 
it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""
class Solution:
    def firstUniqChar(self, s):

        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        myList = {}
        for i in range(len(s)):
            if s[i] not in myList: myList[s[i]] = 1
            else: myList[s[i]] += 1
        for i in range(len(s)): 
            if myList[s[i]] == 1: return i
        return -1