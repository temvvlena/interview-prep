"""
https://leetcode.com/problems/powx-n/
50. Pow(x, n)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        0 1 2 3 4 5 6 7 8 9
        2 2 2 2 2 2 2 2 2 2
        ^
        10 % 2 == 0 --> 2*2

        """
        if n < 0:
            n = abs(n)
            x = 1 / x

        answer = 1
        currentRes = x
        while n > 0:
            if n % 2 == 1:
                answer = currentRes * answer
            currentRes *= currentRes
            n //= 2
        return answer

        """
        Recursion
        if n < 0:
            n = abs(n)
            x = 1/x

        def helper(x, n):
            if n == 0:
                return 1
            half = helper(x, n//2)
            if (n%2==0):
                return half*half
            else:
                return half*half*x

        return helper(x, n)
        """

        """
        TLE
        if n < 0:
            n = abs(n)
            x = 1/x
        number = 1
        for _ in range(n):
            number *= x
        return number
        """
