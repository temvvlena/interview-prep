"""
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
426. Convert Binary Search Tree to Sorted Doubly Linked List

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        inorder traversal


        1 -> 2 -> 3 .... 5 after everything I should point 5 to 1.

        """
        if not root:
            return None

        def inorderTraversal(node):
            nonlocal slowest_constant_pointer, dynamic_pointer
            if node:
                inorderTraversal(node.left)
                if dynamic_pointer:
                    dynamic_pointer.right = node
                    node.left = dynamic_pointer

                else:
                    slowest_constant_pointer = node
                dynamic_pointer = node
                inorderTraversal(node.right)

        slowest_constant_pointer = None
        dynamic_pointer = None

        inorderTraversal(root)
        dynamic_pointer.right = slowest_constant_pointer
        slowest_constant_pointer.left = dynamic_pointer
        return slowest_constant_pointer