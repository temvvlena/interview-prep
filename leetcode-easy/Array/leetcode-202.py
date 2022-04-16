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

        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n not in cycle_members:
            n = get_next(n)

        return n == 1

    """
    def oneByOne(self, number):
        myArray = []
        while number:
            myArray.append(number%10)
            number = number // 10
        return myArray

    def helper(self, number):
        myArray = self.oneByOne(number)
        temp = 0
        for i in myArray: temp += (i**2)
        return temp

    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        turtle, rabbit = n, self.helper(n)
        while turtle != rabbit:
            if rabbit == 1 or turtle == 1:
                return True
            turtle = self.helper(turtle)
            rabbit = self.helper(rabbit)
            rabbit = self.helper(rabbit)
        return False

    def oneByOne(self, number):
        myArray = []
        while number:
            myArray.append(number%10)
            number = number // 10
        return myArray
    def isHappy(self, n: int) -> bool:
        mySet = set()
        while n != 1:
            myArray = self.oneByOne(n)
            temp = 0
            for i in myArray: temp += (i**2)
            n = temp
            if n not in mySet: mySet.add(n)
            else: return False
        return True
    """
