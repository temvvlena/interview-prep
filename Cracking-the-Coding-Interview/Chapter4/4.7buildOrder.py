"""
You are given a list of project and a list of dependencies (which is a list of pairs of projects
where the second project is dependent on the first project.) All of a project's dependecies must
be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
Input:
    projects: a, b, c, d, e, f
    dependencies: (a,d), (f, b), (b,d),(f,a), (d,c)
Output: f, e, a, b, d, c 
Output: f, e, b, a, d, c
"""
from collections import defaultdict

adjacency_list = defaultdict()
adjacency_list['a'] = 'd'
adjacency_list['f'] = 'b'
adjacency_list['b'] = 'd'
adjacency_list['f'] = 'a'
adjacency_list['d'] = 'c'
adjacency_list['c'] = []
adjacency_list['e'] = []

visited_list = defaultdict()
visited_list['a'] = False
visited_list['b'] = False
visited_list['c'] = False
visited_list['d'] = False
visited_list['e'] = False
visited_list['f'] = False

def buildOrder(vertex):
    if not visited_list[vertex]:
        visited_list[vertex] = True
        for neighbor in adjacency_list[vertex]:
            buildOrder(neighbor)
        res.insert(0, vertex)

res = []
for vertex in visited_list:
    buildOrder(vertex)
print(res)