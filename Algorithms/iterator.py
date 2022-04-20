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
