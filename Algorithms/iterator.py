"""
Simple Iterator from list
Iterator from another Iterator
Merge Itrterators in Round Robin fashion
Merge Iterator from iterator of iterators in Round Robin fashion
Merge Iterator from iterator of iterators one after another
Step Iterator using start / end / step => Handle scenarios
Given a list of values, create a infinite cyclic iteratorv
"""

class Iterator:
    def __init__(self, nested_lists):
        self.flattened_list = []
        self.nested_lists = nested_lists

    def flatten(self, nested_lists):
        if not nested_lists: return []
        for nested_list in nested_lists:
            if isinstance(nested_list, int):
                self.flattened_list.append(nested_list)
            else:
                self.flatten(nested_list)
        return self.flattened_list
