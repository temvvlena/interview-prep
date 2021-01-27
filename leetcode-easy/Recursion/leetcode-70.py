"""
https://leetcode.com/problems/climbing-stairs/
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    def __init__(self):
        self.cache = {}
    def climbStairs(self, n):
        if n in self.cache:
            return self.cache[n]
        if n <= 1:
            return 1
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = result
        return result
    # Big O(n)
    """
    Time O(N) and Space O(1)
    if n == 1: return 1
    x, y = 0, 1
    for i in range(0, n): x, y = y, x + y
    return y


    # Formula time complexity O(Logn) and Space complexity(1)
    sqrt5 = sqrt(5)
    fibn = pow(((1+sqrt5)/2), n+1)-pow(((1-sqrt5)/2), n+1)
    return int(fibn/sqrt5)
    """