"""
@author: Temuulen Erdenebulgan
@date: Jan/7/2020
"""
#
# Insertion Sort
# Worst Time runtime is O(N^2). Where N = len(unsorted)
# Base Case runtime is O(N). 
# Average Case runtime is O(N^2).
#
#[1, 3, 2, 3, 4, 5]
def insertionIntegerSort(arr):
    # Let's start from one until the end of the array assuming that the arr[0] is sorted
    for right in range(1, len(arr)):
        currentNumber = arr[right]
        currentPosition = right
        while currentPosition > 0 and arr[currentPosition - 1] > currentNumber:
            arr[currentPosition] = arr[currentPosition - 1]
            currentPosition -= 1
        arr[currentPosition] = currentNumber
    return arr
    
def main():
    cases = [[12, 3, 2, 5, 6], [1, 2, 3, 4, 5], [54, 32, 21, 1] ]
    for case in cases:
        print(insertionIntegerSort(case))

if __name__ == "__main__":
    main()


