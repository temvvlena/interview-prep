"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""
class Solution:
    def intersect(self, nums1, nums2):
        myDict = dict()
        myList = []
        maxLength = max(len(nums1), len(nums2))
        if len(nums1) == maxLength:
            maxLength = nums1
            minLength = nums2
        else:
            maxLength = nums2
            minLength = nums1
        for i in maxLength:
            if i not in myDict:
                myDict[i] = 1
            else:
                myDict[i] += 1
        for i in minLength:
            if i in myDict and myDict[i] > 0:
                myList.append(i)
                myDict[i] -= 1
        return myList
"""
Sort nums1 and nums2.

Initialize i, j and k with zero.

Move indices i along nums1, and j through nums2:

Increment i if nums1[i] is smaller.

Increment j if nums2[j] is smaller.

If numbers are the same, copy the number into nums1[k], and increment i, j and k.

Return first k elements of nums1.

public int[] intersect(int[] nums1, int[] nums2) {
    Arrays.sort(nums1);
    Arrays.sort(nums2);
    int i = 0, j = 0, k = 0;
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] < nums2[j]) {
            ++i;
        } else if (nums1[i] > nums2[j]) {
            ++j;
        } else {
            nums1[k++] = nums1[i++];
            ++j;
        }
    }
    return Arrays.copyOfRange(nums1, 0, k);
}
"""