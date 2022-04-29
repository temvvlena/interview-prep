"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

# Most Optimal Solution
from typing import List


class Solution:
    class Solution:
        def rotateArray(self, index1, index2, nums):
            while index1 < index2:
                nums[index1], nums[index2] = nums[index2], nums[index1]
                index1 += 1
                index2 -= 1

        def rotate(self, nums: List[int], k: int) -> None:
            """
            [5,6,7,4,1,2,3] k = 3
                         ^
                  ^

            [5,6,7,1,2,3,4]


            """
            k %= len(nums)
            n = len(nums)
            self.rotateArray(0, n - 1, nums)
            self.rotateArray(0, k - 1, nums)
            self.rotateArray(k, n - 1, nums)


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a
        return nums


"""
class Solution:
    def rotate(self, nums, k):
        
        Do not return anything, modify nums in-place instead.
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
      
        for i in range(k):
            temp = nums[-1]
            nums.insert(0, nums[-1])
            nums.pop()
        return nums
"""
