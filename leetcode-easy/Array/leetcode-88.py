"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # (n+m)* log(n+m)
        # nums1[:] = sorted(nums1[:m] + nums2)

        # Time complexity : (n+m)
        # Space complexity : m
        nums1_copy = nums1[:m]
        nums1[:] = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        # add the rest
        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
        # Can implement it better without using additional space
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1

        # while there are still elements to compare


"""
while p1 >= 0 and p2 >= 0:
    if nums1[p1] < nums2[p2]:
        nums1[p] = nums2[p2]
        p2 -= 1
    else:
        nums1[p] =  nums1[p1]
        p1 -= 1
    p -= 1

# add missing elements from nums2
nums1[:p2 + 1] = nums2[:p2 + 1]
"""

"""
        # Do not return anything, modify nums1 in-place instead.
        p1 = m - 1
        p2 = n - 1
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, p3 = m - 1, m + n - 1, n - 1
        for p2 in range(m + n - 1, -1, -1):
            if p3 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p3]:
                nums1[p2] = nums1[p1]
                p1 -= 1
            else:
                nums1[p2] = nums2[p3]
                p3 -= 1
