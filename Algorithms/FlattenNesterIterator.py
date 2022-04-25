nestedArray = [
    [[1, [1]], 2, [1, 1]],
    [[1, 2], [3], [4]]
]


class NestedIterator:
    def __init__(self, nestedList):
        self.position = -1

        def flatten(S):
            if not S:
                return S
            if isinstance(S[0], list):
                return flatten(S[0]) + flatten(S[1:])
            return S[:1] + flatten(S[1:])

        self.res = flatten(nestedList)

    def hasNext(self):
        return self.position + 1 < len(self.res)

    def next(self):
        self.position += 1
        return self.res[self.position]


for anArray in nestedArray:
    i, v = NestedIterator(anArray), []

    while i.hasNext():
        v.append(i.next())

    print(v)
