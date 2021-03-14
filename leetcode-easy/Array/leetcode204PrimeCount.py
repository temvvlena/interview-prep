"""
https://leetcode.com/problems/count-primes/
Count Primes
Count the number of prime numbers less than a non-negative number, n.
Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:
Input: n = 0
Output: 0
Example 3:
Input: n = 1
Output: 0
Constraints:
0 <= n <= 5 * 106
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        def isPrime(n):
            if n<=1: return False
            if n<=3: return True
            if n%2==0 or n%3==0: return False
            i=5
            while i*i<=n:
                if (n%i==0 or n%(i+2)==0): return False
                i += 6
            return True
        i=1
        while n>i:
            if isPrime(i):
                res+=1
            i+=1
        return res