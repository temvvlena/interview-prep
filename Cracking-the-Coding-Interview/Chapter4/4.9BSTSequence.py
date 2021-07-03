"""
A binary search tree was created by traversing through an array from left to right and inserting each element.
Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
  2
 / \
1   3
[[2,1,3],[2,3,1]]      
"""
from binarySearchTree import BinarySearchTree

def find_bst_sequences(bst):
    if not bst.root:
        return []
    return helper(bst.root)


def helper(node):
    if not node:
        return [[]]

    right_sequences = helper(node.right)
    left_sequences = helper(node.left)
    print(right_sequences, left_sequences, "I am Groot")
    sequences = []
    for right in right_sequences:
        for left in left_sequences:
            print(left, right, [node.key], sequences, "hello world!")
            sequences = weave(left, right, [node.key], sequences)
    return sequences


def weave(first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        print(results, "i am a result")
        return results

    head = first[0]
    prefix.append(head)
    results = weave(first[1:], second, prefix, results)
    prefix.pop()
    head = second[0]
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    prefix.pop()
    return results


def find_bst_sequences_backtracking(bst):
    if not bst.root:
        return []

    ret_backtracking = []

    def backtracking(choices, weave):
        if not len(choices):
            ret_backtracking.append(weave)
            return

        for i in range(len(choices)):
            nextchoices = choices[:i] + choices[i + 1 :]
            if choices[i].left:
                nextchoices += [choices[i].left]
            if choices[i].right:
                nextchoices += [choices[i].right]
            backtracking(nextchoices, weave + [choices[i].key])

    backtracking([bst.root], [])
    return ret_backtracking


testable_functions = [find_bst_sequences, find_bst_sequences_backtracking]


def test_find_bst_sequences():
    for find_bst in testable_functions:
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        sequences = find_bst(bst)
        assert [2, 1, 3] in sequences
        assert [2, 3, 1] in sequences
        assert len(sequences) == 2


def example():
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    #bst.insert(5)
    #bst.insert(12)
    # bst.insert(11);
    # bst.insert(14);

    sequences = find_bst_sequences(bst)
    print(sequences)

    sequences = find_bst_sequences_backtracking(bst)
    print(sequences)


if __name__ == "__main__":
    example()