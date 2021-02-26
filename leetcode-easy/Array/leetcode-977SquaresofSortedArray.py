"""
https://leetcode.com/problems/squares-of-a-sorted-array/
Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        First Solution 
        NLogIn and N
        for i in range(len(nums)): nums[i] = nums[i]**2
        return sorted(nums)
        """
        """
        Second Solution
        Intuition
        Since the array A is sorted, loosely speaking it has some negative elements with squares in decreasing order, 
        then some non-negative elements with squares in increasing order.
        For example, with [-3, -2, -1, 4, 5, 6], we have the negative part [-3, -2, -1] with squares [9, 4, 1], and the 
        positive part [4, 5, 6] with squares [16, 25, 36]. Our strategy is to iterate over the negative part in reverse, 
        and the positive part in the forward direction.
        """
        n = len(nums)
        res = [0]*n
        left = 0
        right = n - 1
        for i in range(n-1, -1, -1):
            if abs(nums[left])<abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            res[i] = square * square
        return res