"""
https://leetcode.com/problems/network-delay-time/
Network Deloy
"""
from collections import defaultdict
from heapq import heappop, heappush
def networkDelayTime(times, n: int, k: int) -> int:
    graph = defaultdict(list)
    for source, destination, weight in times:
        graph[source].append((destination, weight))
    q = [(0,k)]
    visited = set()
    max_cost = 0
    while q:
        cost, node = heappop(q)
        if node in visited:
            continue
        visited.add(node)
        max_cost = max(max_cost, cost)
        neighbors = graph[node]
        for neighbor in neighbors:
            new_node, new_cost = neighbor
            if new_node not in visited:
                curr_cost = cost+new_cost
                heappush(q, (curr_cost, new_node))
    return max_cost if len(visited) == n else -1

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
