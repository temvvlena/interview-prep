"""
https://leetcode.com/problems/range-sum-of-bst/
Range Sum of BST
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Constraints:
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Let's try Depth first search
# Time and Space Complexity O(N)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def helper(root):
            if root is None: return 
            if L<=root.val<=R:
                self.ans += root.val
            if L < root.val:
                helper(root.left)
            if root.val < R:
                helper(root.right)
        self.ans = 0
        helper(root)
        return self.ans
"""
    Solution 1
    Breath First Search
    from collections import deque
    class Solution:
        def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
            q = deque()
            q.append(root)
            res = []
            while q:
                for i in range(len(q)):
                    cur = q.popleft()
                    res.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            counter = 0
            for i in res:
                if L<=i<=R:
                    counter += i
            return counter

    Solution 2
    More Optimal BFS Solution
    q = deque()
    q.append(root)
    counter = 0
    while q:
        for i in range(len(q)):
            cur = q.popleft()
            if L<=cur.val<=R: 
                counter += cur.val
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    return counter
    
    Solution 3
    def helper(root):
        if root is None: return []
        return helper(root.left) + [root.val] + helper(root.right)
    counter = 0
    for i in helper(root):
        if L<=i<=R:
            counter += i
    return counter

    Solution 4
    More optimal depth first solution
"""