"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        q = deque([root])
        ans = []
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                q.extend(node.children)
            ans.append(temp)
        return ans