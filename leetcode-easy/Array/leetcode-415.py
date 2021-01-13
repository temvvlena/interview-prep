"""
https://leetcode.com/problems/add-strings/
Given two non-negative integers num1 and num2 represented as string, 
return the sum of num1 and num2.
Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1, num2):
        #   3
        # 232
        # 525
        # Time complexity O(Max(N1, N2)) and Space complexity is max(N1, N2)
        carry = 0
        res = ''
        num1, num2 = num1[::-1], num2[::-1]
        i, j = 0, 0
        while i < len(num1) or j < len(num2):
            dig1  = int(num1[i]) if i < len(num1) else 0
            dig2  = int(num2[i]) if i < len(num2) else 0
            sumNumber = int(dig1) + int(dig2) + carry   
            carry, number = sumNumber // 10, sumNumber % 10
            res += str(number)
            i += 1
            j += 1
        if carry != 0:
            res += str(carry)
        return res[::-1]
        
     