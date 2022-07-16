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
    def calculate(self, s: str) -> int:
        stack = []
        index = 0
        currentNumber = 0
        operation = "+"
        while index < len(s):
            if s[index].isnumeric():
                currentNumber = currentNumber * 10 + int(s[index])
            if s[index] in "*/+-" or index == len(s) - 1:
                if operation == "-":
                    stack.append(-currentNumber)
                elif operation == "+":
                    stack.append(currentNumber)
                elif operation == "*":
                    stack.append(stack.pop() * currentNumber)
                else:
                    temp = stack.pop()
                    if temp < 0:
                        stack.append(-(-temp // currentNumber))
                    else:
                        stack.append(temp // currentNumber)
                operation = s[index]
                currentNumber = 0
            if s[index] == " ":
                pass
            index += 1
        return sum(stack)

        # It can be optimized using one loop. With time (N) and Space(1). 
        # Will work on it later
