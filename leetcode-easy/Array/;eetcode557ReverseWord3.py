"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"
"""

# Most optimal solution


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        s = s.split(" ")
        for aWord in s:
            res.append(aWord[::-1])
        return " ".join(res)

# Using two pointers, Thrivial approach


class Solution:
    def helper(self, word):
        res = []
        for aWord in word:
            res.append(aWord)
        left, right = 0, len(res)-1
        while left <= right:
            res[left], res[right] = res[right], res[left]
            left, right = left + 1, right - 1
        return "".join(res)

    def reverseWords(self, s: str) -> str:
        res = []
        s = s.split(" ")
        for aWord in s:
            res.append(self.helper(aWord))
        return " ".join(res)
