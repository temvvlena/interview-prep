"""
https://leetcode.com/problems/sort-array-by-parity/
Given an array A of non-negative integers, return an array consisting of all 
the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.
Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""
# Time O(n) and Space O(1)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = 0 
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[slow], nums[i]=nums[i], nums[slow]
                slow += 1
        return nums
# Time and Space O(n)
class Solution:
    def sortArrayByParity(self, A):
        myList = list()
        for i in A:
            if i % 2 == 0: myList.append(i)
        for i in A:
            if i % 2 != 0: myList.append(i)
        return myList
                
