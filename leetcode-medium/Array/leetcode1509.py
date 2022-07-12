"""
Minimum Difference Between Largest and Smallest Value in Three Moves
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.
Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.
Example 1:
Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:
Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.
Time NLog Space Constant
"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        res = 10**10
        print(nums)
        for a, b in zip(nums[:4], nums[-4:]):
            print(b, a)
            res = min(res, b-a)
        return res