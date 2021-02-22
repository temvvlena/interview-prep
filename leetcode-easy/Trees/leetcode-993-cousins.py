"""
https://leetcode.com/problems/cousins-in-binary-tree/
Cousins in Binary Tree
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
Constraints:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Time and Space O(N)
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = collections.deque([root])
        while q:
            parent = {}
            for _ in range(len(q)):
                node = q.popleft() 
                if node.left:
                    q.append(node.left)
                    parent[node.left.val] = node
                if node.right:
                    q.append(node.right)
                    parent[node.right.val] = node
            # XOR
            # 1 ^ 0 = 1, 0 ^ 1 = 1, 1 ^ 1 = 0, 0 ^ 0 = 0
            if (x in parent) ^ (y in parent): return False
            if x in parent and y in parent:
                if parent[x] == parent[y]: return False
                else: return True
        return False        