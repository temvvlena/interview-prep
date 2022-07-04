"""
https://leetcode.com/problems/kth-missing-positive-number/
1539. Kth Missing Positive Number
"""


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        j = 0
        res = []
        for i in range(arr[-1] + k):
            if j < len(arr) and i + 1 != arr[j]:
                res.append(i + 1)
            elif j < len(arr):
                j += 1
            else:
                res.append(i + 1)
        return res[k - 1]


class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        if k < arr[0]:
            return k
        res = []
        j = 0
        for i in range(arr[-1] + k):
            if j < len(arr) and i + 1 != arr[j]:
                res.append(i + 1)
            elif j < len(arr):
                j += 1
            elif j == len(arr):
                res.append(i + 1)
            else:
                break
        if len(res) == 0:
            return arr[-1] + k
        return res[k - 1]


"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k"""
