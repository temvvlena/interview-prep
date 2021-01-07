"""
https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment that could only 
store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
"""
class Solution:
    def reverse(self, x):
        temp = x
        rev = 0
        if x<0:  x=-x
        while(x):
            rem = x%10
            rev = (rev*10) + rem
            x = x//10
        if rev > pow(2, 31): return 0
        else:
            if temp>=0: return rev
            else: return (-1*rev)
"""
# Time Complexity & Space LogN
if x == 0: return 0
convertingString = str(x)
negativeNumber = False
if convertingString[0] == "-":
    negativeNumber = True
    convertingString = convertingString[1:]
convertingString = convertingString[::-1]
convertingInteger = int(convertingString)
if negativeNumber: 
    convertingInteger = convertingInteger * - 1
    if convertingInteger > 2 ** 31 -1 or convertingInteger < -2 ** 31: return 0
if convertingInteger > 2 ** 31 -1 or convertingInteger < -2 ** 31: return 0
return convertingInteger
"""