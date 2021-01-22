"""
https://leetcode.com/problems/add-binary/
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
        return bin((int(a, 2)+int(b, 2)))[2:]
            
        """"
        a, b, mySum = int(a, 2), int(b, 2), 0
        while b:
            answer = a ^ b
            carry = (a & b) << 1
            a, b = answer, carry
        return str(bin(a)[2:])
        """
    
    """
    1
    
    11      2 = 10
     1
   ---
   100 
    
    XOR     AND
    11       11
     1        1
------     -------
    10       01 << 1 -> 10  --> 2, 2 (Decimal)
    
    10      10
    10      10
    --     ---
    00      10 --> 100  --> 
    
    00      00
   100     100 
   ---     ---
   100     000
    
    """
            