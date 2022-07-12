"""
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:
Input: nums = []
Output: []
Example 3:
Input: nums = [0]
Output: []
"""
# Takes a list and returns list of lists
# Time Complexity O(nLogn * n), so overall O(n^2)
# Main idea here is the same as twoSum, but one should consider duplicates
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        def helper(myList, first, res):
            leftPointer, rightPointer = first+1, len(myList)-1
            while rightPointer > leftPointer:
                addition = myList[rightPointer]+myList[leftPointer]+nums[first]
                if addition>0:
                    rightPointer -= 1
                elif addition <0:
                    leftPointer += 1
                else: 
                    res.append([nums[first], myList[leftPointer], myList[rightPointer]])
                    leftPointer += 1
                    rightPointer -= 1
                    while rightPointer > leftPointer and nums[leftPointer] == nums[leftPointer-1]:
                        leftPointer += 1
        # main function
        firstPointer = 0
        res = []
        nums.sort()
        while firstPointer <= len(nums)-1:
            if nums[firstPointer] > 0: break
            if firstPointer == 0 or nums[firstPointer-1] != nums[firstPointer]:
                helper(nums, firstPointer, res)
            firstPointer += 1
        return res