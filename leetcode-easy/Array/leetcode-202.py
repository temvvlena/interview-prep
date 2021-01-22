"""
https://leetcode.com/problems/happy-number/
Happy Number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        # Time LogN and Space LogN
        def next_number(n):
            mySum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                mySum += digit ** 2
            return mySum
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_number(n)
        return n == 1
    
    
        """
        # Time LogN and Space 1
        def next_number(n):
            mySum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                mySum += digit ** 2
            return mySum
        
        slow, fast = n, next_number(n)
        while fast != 1 and slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))
        return fast == 1
        
        """
        