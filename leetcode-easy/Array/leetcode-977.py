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
# O(N) Solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right, left = len(nums)-1, 0 
        newList = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                newList[i] = nums[right]**2 
                right -= 1
            else:
                newList[i] = nums[left]**2
                left += 1
        return newList

# NLogN Solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #NLogN Solution
        for i in range(len(nums)): nums[i] = nums[i]**2
        return sorted(nums)