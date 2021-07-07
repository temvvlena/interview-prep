"""
# VISUAL OF TEST GRAPH:

A -- B
|    |
C -- D
|
E -- F -- G -- H
     | \
     O   I -- J -- K
              |
              L

P -- Q
|  /
R

"""


from collections import deque
# BFS
def search(g, start, end):
    if start == end: return True
    q = deque()
    q.append(start)
    visited = set()
    while q:
        node = q.popleft()
        for adjacent in g[node]:
            if adjacent not in visited:
                if adjacent == end: return True
                else: q.append(adjacent)
        visited.add(node)
    return False

#DFS
def is_route(g, start, end, visited=None):
    if not visited: visited = set()
    for node in g[start]:
        if node not in visited:
            visited.add(node)
            if node == end or is_route(g, node, end, visited): return True
    return False

g = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"],
    "F": ["E", "O", "I", "G"],
    "G": ["F", "H"],
    "H": ["G"],
    "I": ["F", "J"],
    "O": ["F"],
    "J": ["K", "L", "I"],
    "K": ["J"],
    "L": ["J"],
    "P": ["Q", "R"],
    "Q": ["P", "R"],
    "R": ["P", "Q"],
    }
start, end = "A", "L"
print(is_route(g, start, end))
