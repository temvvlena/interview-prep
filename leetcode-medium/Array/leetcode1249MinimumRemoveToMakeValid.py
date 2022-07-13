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

"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
1249. Minimum Remove to Make Valid Parentheses
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def delete_invalid_closing(string, open_symbol, close_symbol):
            sb = []
            balance = 0
            for c in string:
                if c == open_symbol:
                    balance += 1
                if c == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(c)
            return "".join(sb)

        # Note that s[::-1] gets the reverse of s.
        s = delete_invalid_closing(s, "(", ")")
        s = delete_invalid_closing(s[::-1], ")", "(")
        return s[::-1]

    def minRemoveToMakeValid2(self, myString: str) -> str:
        res = []
        myString = list(myString)
        for index, value in enumerate(myString):
            if value == ")" and not res:
                res.append([value, index])
            elif value.isalpha():
                continue
            elif res and value == ")" and res[-1][0] == "(":
                res.pop()
            else:
                res.append([value, index])
        mySet = []
        for char, index in res:
            mySet.append(index)
        final = []
        for index in range(len(myString)):
            if index in mySet:
                continue
            else:
                final.append(myString[index])
        return "".join(final)
