from iterator import *


def test_flatten():
    input = [
        [[9, 4, 3], 7, [[2, 6], 4, [[1]]], [[[]], [7], 6, [5, [], 0]], 2, [[1], 5, 9]],
        [[1, 2, 3]],
        [],
        [[]]
    ]
    expected = [
        [9, 4, 3, 7, 2, 6, 4, 1, 7, 6, 5, 0, 2, 1, 5, 9],
        [1, 2, 3],
        [],
        []
    ]
    for index in range(len(input)):

        assert Iterator(input[index]).flatten(input[index]) == expected[index]