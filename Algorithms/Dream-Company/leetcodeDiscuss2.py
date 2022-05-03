"""
Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, the ID of
the user making the access, and the resource ID.

The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.

Example:
logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]

Example 2:
logs2 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]

Example 3:
logs3 = [
    ["300", "user_10", "resource_5"]
]

Write a function that returns within a sliding window of K, what's the maximum number of times a single resource is accessed.
Assuming for window of 300 seconds, the output for the above data would be:

(3, 'resource_3')
(4, 'resource_3')
(1, 'resource_5')


Write a function that takes the logs as input, builds the transition graph and returns it as an adjacency list with
probabilities. Add __START__ and __END__ states.

Specifically, for each resource, we want to compute a list of every possible next step taken by any user, together with
the corresponding probabilities. The list of resources should include __START__ but not __END__, since by
definition __END__ is a terminal state.

Expected output for logs1:
transition_graph(logs1) # =>
{
    '__START__': {'resource_1': 0.25, 'resource_2': 0.125, 'resource_3': 0.5, 'resource_6': 0.125},
    'resource_1': {'resource_6': 0.333, '__END__': 0.667},
    'resource_2': {'__END__': 1.0},
    'resource_3': {'__END__': 0.4, 'resource_1': 0.2, 'resource_2': 0.2, 'resource_3': 0.2},
    'resource_4': {'__END__': 1.0},
    'resource_5': {'resource_4': 1.0},
    'resource_6': {'__END__': 0.5, 'resource_5': 0.5}
}

 wow! exact same questions were asked to me a day ago. In Round 2, the question was to initially implement the
 Interleaving function only. Later he asked me to implement ListIterator, RangeIterator, and then Interleaving Iterator.
  I was unable to complete the Interleaving Iterator. The interviewer keep on interrupting me to think of a O(1) space
  solution which I said I can't think of. FYI, the standard solution that I saw people have implemented is the Queue Solution.
  In Round3, there were two follow-ups. One was the parent-child one and there was one more as well.
  I could barely complete the first follow-up but the interviewer seemed satisfied. Good to know that you got the offer.
  It gives me hope as well.
"""

"""


logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]
{
    '__START__': {'resource_1': 0.25, 'resource_2': 0.125, 'resource_3': 0.5, 'resource_6': 0.125},
    'resource_1': {'resource_6': 0.333, '__END__': 0.667},
    'resource_2': {'__END__': 1.0},
    'resource_3': {'__END__': 0.4, 'resource_1': 0.2, 'resource_2': 0.2, 'resource_3': 0.2},
    'resource_4': {'__END__': 1.0},
    'resource_5': {'resource_4': 1.0},
    'resource_6': {'__END__': 0.5, 'resource_5': 0.5}
}
"""

"""
Second Question:
[[1,2,3],[4,5],[6],[],[7,8,9]]
"""

# myList = \
#     [
#         [1, 2, 3],
#         [4, 5],
#         [6],
#         [],
#         [7, 8, 9]
#     ]
# res = []
# for row in range(len(myList)):
#     curRowLength = len(myList[row])
#     for col in range(len(myList[0])):
#         if curRowLength > col:
#             res.append(myList[row][col])
#         else:
#             continue
myList = \
    [
        [1, [2, [3]]],
        [4, 5],
        [6],
        [],
        [7, 8, 9]
    ]


def flatten_array(nums):
    if not nums:
        return nums
    if isinstance(nums[0], list):
        return flatten_array(nums[0]) + flatten_array(nums[1:])
    return nums[:1] + flatten_array(nums[1:])


print(flatten_array(myList))
