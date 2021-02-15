"""
Find The Duplicates
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2
Constraints:

[time limit] 5000ms

[input] array.integer arr1

1 ≤ arr1.length ≤ 100
[input] array.integer arr2

1 ≤ arr2.length ≤ 100
[output] array.integer
"""

# Brute Force approach
# Time nLogN and space N
def find_duplicates(arr1, arr2):
    return sorted(list(set(arr1)&set(arr2)))

# Time complexity O (n+m)
# Space complexity O(N)
def find_duplicates(arr1, arr2):
  i, j, dup = 0, 0, []
  while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]: 
      dup.append(arr1[i])
      i += 1
      j += 1
    elif arr1[i] > arr2[j]: j += 1
    else: i += 1
  return dup
    
# Solution 2

# Time NLogN and Space O N
def find_duplicates(arr1, arr2):
  duplicates = []
  for i in arr1:
    if binarySearch(arr2, i) != -1: duplicates.append(i)
  return duplicates

def binarySearch(arr, num):
  begin, end = 0, len(arr)-1
  while begin <= end:
    mid = (begin + end)//2
    if arr[mid] < num:
      begin = mid + 1
    elif arr[mid] == num: return mid
    else: end = mid - 1
  return -1