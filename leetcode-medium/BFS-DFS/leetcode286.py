"""
https://leetcode.com/problems/walls-and-gates/submissions/
Walls and Gates
"""

from collections import deque


def wallsAndGates(rooms) -> None:
    print(rooms, "Before")
    if rooms == [[-1]]: return [[-1]]

    q = deque()
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                q.append((row, col))
    while q:
        row, col = q.popleft()
        for direction in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            r, c = row + direction[0], col + direction[1]
            if 0 <= r < len(rooms) and 0 <= c < len(rooms[0]) and rooms[r][c] == 2147483647:
                rooms[r][c] = rooms[row][col] + 1
                q.append((r, c))
    print(rooms, "After")


print(wallsAndGates([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], \
                     [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]))
