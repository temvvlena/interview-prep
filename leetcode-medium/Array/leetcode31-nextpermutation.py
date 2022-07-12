"""
https://leetcode.com/problems/next-permutation/
Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:
Input: nums = [1]
Output: [1]
"""
#1 , 5, 8, 4, 7, 6, 5, 3, 1
#          ^
#                   ^
class Solution:
    def reverse(self, left, nums):
        right = len(nums)-1
        while right > left:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums)-1
            while nums[j]<=nums[i]:
                j -= 1
            print(i, j)
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        self.reverse(i+1, nums)