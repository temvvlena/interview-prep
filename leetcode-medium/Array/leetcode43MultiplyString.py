"""
https://leetcode.com/problems/multiply-strings/
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1, res2 = 0, 0
        for i in num1: res1 = res1*10 + (ord(i)-ord('0'))
        for i in num2: res2 = res2*10 + (ord(i)-ord('0'))
        return str(res1*res2)