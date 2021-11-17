"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/
Check If N and Its Double Exist

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:
Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M
"""
# N^2 Solution
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        res, count, myList = False, 0, []
        for i in arr:
            if i != 0: myList.append(i)
            else: count += 1
        for i in range(len(myList)):
            for j in range(i+1, len(myList)):
                if myList[i] / myList[j] == 0 or myList[j] * 2 == myList[i] or myList[i] * 2 == myList[j]: res = True
        if count >=2: return True
        return res