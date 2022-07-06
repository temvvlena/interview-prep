"""
153. Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order 
is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums, return the minimum element of this array.

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""
class Solution:
    def findMin(self, nums):
        """
        # My first Brute Force Solution. It will take O(n*log(n)) on average
        nums.sort()
        return nums[0]
        # Or it could be return min(nums) O(n)
        # O(n) would work too
        
        # However I want to solve this using Binary Search Algorithm O(log*n)
        I should figure out the inflection point.
        """
        # Edge case
        if len(nums) == 1:
            return nums[0]
        left = 0 
        right = len(nums) - 1
        # Another edge case could be it might have already been sorted
        if nums[right] > nums[left]:
            return nums[left]
        while left <= right:
            mid = (left + right) // 2
            # I have to check 2 cases. The mid point can be the smallest or not
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[left]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1
            # Time Complexity (Log N) Space Complexity Big O(1)