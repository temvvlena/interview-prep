"""
https://leetcode.com/problems/balance-a-binary-search-tree/submissions/
1382. Balance a Binary Search Tree
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Solution 1
        """

        def convert_tree_list(tree):
            if tree:
                convert_tree_list(tree.left)
                tree_as_list.append(tree.val)
                convert_tree_list(tree.right)

        def create_binary_tree(aList):
            if len(aList) < 1:
                return None
            mid = len(aList) // 2
            root = TreeNode(aList[mid])
            root.left = create_binary_tree(aList[:mid])
            root.right = create_binary_tree(aList[mid + 1:])
            return root

        tree_as_list = []
        convert_tree_list(root)
        result = create_binary_tree(tree_as_list)
        return result

        """
        Solution 2
        def convert_tree_list(tree):
            q = deque()
            q.append(tree)
            answer = []
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    answer.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            return answer

        def create_binary_tree(aList):
            if len(aList) < 1:
                return None
            mid = len(aList) // 2
            root = TreeNode(aList[mid])
            root.left = create_binary_tree(aList[:mid])
            root.right = create_binary_tree(aList[mid+1:])
            return root


        tree_as_list = convert_tree_list(root)
        sorted_tree = sorted(tree_as_list)
        result = create_binary_tree(sorted_tree)
        return result        
        """

        """
        Solution 3
        def convert_tree_list(tree):
            q = deque()
            q.append(tree)
            answer = []
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    answer.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            return answer

        def add(node, number):
            if node == None: 
                return TreeNode(number)

            if node.val < number:
                if node.right is None:
                    node.right = TreeNode(number)
                else:
                    add(node.right, number)
            else:
                if node.left is None:
                    node.left = TreeNode(number)
                else:
                    add(node.left, number)
            return node


        def create_binary_tree(myTree, cur):
            if len(myTree) < 1:
                return cur
            mid = len(myTree) // 2
            cur = add(cur, myTree[mid])
            create_binary_tree(myTree[:mid], cur)
            create_binary_tree(myTree[mid+1:], cur)
            return cur

        tree_as_list = convert_tree_list(root)
        sorted_tree = sorted(tree_as_list)
        result = create_binary_tree(sorted_tree, None)

        return result
        """
