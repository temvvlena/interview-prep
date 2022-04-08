"""
https://leetcode.com/problems/add-binary/
Add Binary
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        #print(int(a, 2) + int(b, 2))
        #return '{0:b}'.format(int(a, 2) + int(b, 2))

        """
        Your input
        "1111"
        "1011"

         1
        1111  line 16
        1101  line 17
        ----
        01

        11 a  --> 11
         1 b  --> 1
        """
        res = []
        carry = 0
        a = a[::-1]
        b = b[::-1]
        i = 0
        j = 0
        temp = 0
        while i < len(a) or j < len(b):
            temp = carry
            if i < len(a):
                temp += int(a[i])
            if j < len(b):
                temp += int(b[j])
            carry = 0
            if temp == 2:
                carry = 1
                temp = 0
            if temp == 3:
                carry = 1
                temp = 1
            res.append(str(temp))
            i += 1
            j += 1
        if carry == 1:
            res.append(str(carry))
        return "".join(res[::-1])
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
            