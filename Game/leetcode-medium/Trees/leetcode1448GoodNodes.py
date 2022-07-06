"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Count Good Nodes in Binary Tree
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.
Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""
# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValue, res):
            if not node: return 0
            if node.val>= maxValue: res = 1 
            if node.val< maxValue: res = 0
            maxValue = max(maxValue, node.val)
            res += dfs(node.left, maxValue, res)
            res += dfs(node.right, maxValue, res) 
            return res
        return dfs(root, root.val, res=1)
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append([root, root.val])
        counter = 0
        while q:
            cur, max_so_far = q.popleft()
            if max_so_far <= cur.val:
                counter += 1
            if cur.left:
                q.append((cur.left, max(cur.val, max_so_far)))
            if cur.right:
                q.append((cur.right, max(max_so_far, cur.val)))
        return counter
