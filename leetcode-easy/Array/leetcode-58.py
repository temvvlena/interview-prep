"""
https://leetcode.com/problems/length-of-last-word/
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.
Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0
"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        # Time Complexity(N) and Space (1)
        p, length = len(s), 0
        while p > 0:
            p -= 1
            # we're in the middle of the last word
            if s[p] != ' ':
                length += 1
            # here is the end of last word
            elif length > 0:
                return length
        return length
        """ 
        # Time complexity O(N) and Space complexity O(N)
        if s == " " or s == "": return 0
        myList = list()
        for i in s.strip().split(" "): myList.append(i)
        return len(myList[-1])
    