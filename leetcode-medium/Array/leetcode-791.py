from collections import Counter


def customSort(order, s):
    counter = Counter(s)
    ans = []

    for char in order:
        ans.append(char * counter[char])
        counter[char] = 0

    for char in counter:
        ans.append(char * counter[char])

    return "".join(ans)


# the remaining can be returned in any order
print(customSort("cba", "aabbbcccefddk"))
