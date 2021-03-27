"""
https://leetcode.com/problems/power-of-three/
Power of Three
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
Example 1:
Input: n = 27
Output: true
Example 2:
Input: n = 0
Output: false
Example 3:
Input: n = 9
Output: true
Example 4:
Input: n = 45
Output: false
"""

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        temp = int(math.log10(n)/math.log10(3))
        if temp - math.log10(n)/math.log10(3) == 0: return True
        else: return False
 
        """
        if n == 1: return True
        while n > 2:
            if n % 3 != 0: return False
            n /= 3
            if n == 1: return True
        return False
        """