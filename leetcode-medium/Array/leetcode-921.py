"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
921. Minimum Add to Make Parentheses Valid
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = bal = 0
        for symbol in s:
            if symbol == "(":
                bal += 1
            else:
                bal -= 1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal

    def minAddToMakeValidFirstTry(self, s: str) -> int:
        stack = []
        for index, char in enumerate(s):
            if char == ")" and not stack:
                stack.append(char)
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
