"""
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
1007. Minimum Domino Rotations For Equal Row
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
"""

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def helper(target, tops, bottoms):
            counter = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return maxNumber
                elif tops[i] != target:
                    counter += 1
            return counter
        
        maxNumber = 20000
        minNumber = maxNumber
        minNumber = min(
            helper(tops[0], tops, bottoms),
            helper(bottoms[0], tops, bottoms),
            helper(tops[0], bottoms, tops),
            helper(bottoms[0], bottoms, tops),
        )
        if minNumber == maxNumber: return -1
        else: return minNumber