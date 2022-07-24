"""
https://leetcode.com/problems/diagonal-traverse/
498. Diagonal Traverse
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        myDictionary = {}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row + col not in myDictionary:
                    myDictionary[row + col] = [mat[row][col]]
                else:
                    myDictionary[row + col].append(mat[row][col])
        ans = []
        for aKey, aValue in myDictionary.items():
            if aKey % 2 == 0:
                for num in aValue[::-1]:
                    ans.append(num)
            else:
                for num in aValue:
                    ans.append(num)
        return ans
