"""
https://leetcode.com/problems/intersection-of-two-arrays/submissions/
349. Intersection of Two Arrays
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
        """
        if not nums1 or not nums2:
            return []
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        if len(set_nums1) > len(set_nums2):
            longest_set = set_nums1
            shortest_set = set_nums2
        else:
            longest_set = set_nums2
            shortest_set = set_nums1

        res = []

        for num in longest_set:
            if num in shortest_set:
                res.append(num)
        return res"""
