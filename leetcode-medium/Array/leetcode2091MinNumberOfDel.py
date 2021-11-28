"""
https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
Removing Minimum and Maximum From Array

You are given a 0-indexed array of distinct integers nums.
There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.
A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.
Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

Example 1:
Input: nums = [2,10,7,5,4,1,8,6]
Output: 5
Explanation: 
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.

Example 2:
Input: nums = [0,-4,19,1,8,-2,-3,5]
Output: 3
Explanation: 
The minimum element in the array is nums[1], which is -4.
The maximum element in the array is nums[2], which is 19.
We can remove both the minimum and maximum by removing 3 elements from the front.
This results in only 3 deletions, which is the minimum number possible.

Example 3:
Input: nums = [101]
Output: 1
Explanation:  
There is only one element in the array, which makes it both the minimum and maximum element.
We can remove it with 1 deletion.
"""

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        u = max(nums)
        v = min(nums)
        x = 0
        y = 0
        for i in range(len(nums)):
            if nums[i] == u:
                x = i
            if nums[i] == v:
                y = i
        if x > y:
            x, y = y, x
        ans = float('inf')
        ans = min(ans, y + 1)
        ans = min(ans, len(nums) - x)
        ans = min(ans, len(nums) - y + x + 1)
        return ans
    
        """
        if len(nums) == 1: return 1
        if len(nums) == 2: return 2
        
        res = 0
        
        temp1 = min(nums)
        minValue = nums.index(temp1)
        
        temp2 = max(nums)
        maxValue = nums.index(temp2)
        
        countForwardMin, countBackwardMin = 0, 0 
        countForwardMax, countBackwardMax = 0, 0
        
        for i in range(len(nums)):
            if i == minValue: break
            else: countForwardMin += 1
        
        for i in range(len(nums)-1, -1, -1):
            if i == minValue: break
            else: countBackwardMin += 1
            
        if countForwardMin > countBackwardMin:
            temp = countBackwardMin+1
            res += temp
            nums = nums[0:i]
        else:
            temp = countForwardMin+1
            res += temp
            nums = nums[temp+1::]
    
    
        for i in range(len(nums)):
            if i == maxValue: break
            else: countForwardMax += 1
        
        for i in range(len(nums)-1, -1, -1):
            if i == maxValue: break
            else: countBackwardMax += 1
        
        if countForwardMax > countBackwardMax:
            temp = countBackwardMax+1
            res += temp
            nums = nums[0:i]
        else:
            temp = countForwardMax+1
            res += temp
            nums = nums[temp+1::]
        
        return res
        """
                    