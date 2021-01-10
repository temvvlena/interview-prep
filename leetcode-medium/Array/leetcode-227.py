"""
https://leetcode.com/problems/basic-calculator-ii/
Basic Calculator II
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5
"""

class Solution:
    def calculate(self, s):
        """
        Using Stack, time and space complexity will be O(N)
        s = "3+2*2"
                |
        [3, 4] = 7
        3-2/2*2
        [3, -2] = 1
        myStack = [3, ]
        """
        if len(s) == 1: return s[0]
        num, i, myStack, sign = 0, 0, [], "+"
        while i < len(s):
            if s[i].isdigit(): num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s)-1:
                if sign == "+": myStack.append(num)
                elif sign == "-": myStack.append(-num)
                elif sign == "*": myStack.append(myStack.pop()*num)
                else: myStack.append(int(myStack.pop()/num))
                num, sign = 0, s[i]        
            i += 1
        return sum(myStack)

        # It can be optimized using one loop. With time (N) and Space(1). 
        # Will work on it later
