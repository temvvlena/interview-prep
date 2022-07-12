"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        remove = list()
        stack = []
        for i, c in enumerate(s):
            if c not in "()": continue
            if c=="(": stack.append(i)
            elif not stack: remove.append(i)
            else: stack.pop()
        remove += stack
        for i in remove[::-1]: s.pop(i)
        return "".join(s)


"""
Solution 2
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def delete_invalid_closing(string, open_symbol, close_symbol):
            sb, balance = [], 0
            for c in string:
                if c == open_symbol: balance += 1
                if c == close_symbol:
                    if balance == 0: continue
                    balance -= 1
                sb.append(c)
            return "".join(sb)
        s = delete_invalid_closing(s, "(", ")")
        s = delete_invalid_closing(s[::-1], ")", "(")
        return s[::-1]
"""