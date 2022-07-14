"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
314. Binary Tree Vertical Order Traversal
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        orderedArray = []
        q = deque()
        q.append((root, 0))
        while q:
            for _ in range(len(q)):
                node, val = q.popleft()
                orderedArray.append([node.val, val])
                if node.left:
                    q.append((node.left, val - 1))
                if node.right:
                    q.append((node.right, val + 1))
        orderedArray.sort(key=lambda x: x[1])
        myDict = {}
        for anArray in orderedArray:
            if anArray[-1] not in myDict:
                myDict[anArray[-1]] = [anArray[0]]
            else:
                myDict[anArray[-1]].append(anArray[0])
        final_answer = []
        for aKey, aValue in myDict.items():
            final_answer.append(aValue)
        return final_answer
