"""
https://leetcode.com/problems/valid-mountain-array/
Valid Mountain Array
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2: return False
        N, i = len(arr),  0 
        while i < N - 1 and arr[i] < arr[i+1]: i += 1
        if i == 0 or i == N - 1: return False
        while i < N - 1 and arr[i] > arr[i+1]:i += 1
        return i == N - 1