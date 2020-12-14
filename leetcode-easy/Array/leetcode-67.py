"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a, b):
        x, y = int(a, 2), int(b, 2)
        while y:
            addition = a ^ b
            carry = (a & b) << 1
            x, y = addition, carry
        return bin(x)[2:]
        