example = {
    1: {
        "table": {
            "res": 200,
            "ji": 1000
        },
        "column": 3,
        "row": 2,
        "addition": 1000
    },
    2: {
        "table": 12,
        "column": 100,
        "row": 200
    }
}


# Output: [[1,10,3,2,1000][2,12,100,200]]


def flatten_dictionary(my_dictionary):
    output = []
    for aKey, aValue in my_dictionary.items():
        item = [aKey]
        for value in aValue.values():
            if isinstance(value, dict):
                for i in value.values():
                    item.append(i)
            else:
                item.append(value)
        output.append(item)
    return output


# print(flatten_dictionary(example))


example2 = {
    1: {
        "table":
            {
                "res": 200,
                "ji":
                    {
                        "hi": 11,
                        "bye": 22,
                        "say":
                            {
                                "fef": 11
                            }
                    }
            },
        "column": 3,
        "row": 2,
        "addition": 1000
    },
    2:
        {
            "table": 12,
            "column": 100,
            "row": 200
        }
}


def flatten_dictionary2(my_dictionary):
    output2 = []
    for aKey, aDictionary in my_dictionary.items():
        item = [aKey]
        helper(aDictionary, item)
        output2.append(item)
    return output2


def helper(myDict, item):
    for aKey, aValue in myDict.items():
        if isinstance(aValue, dict):
            helper(aValue, item)
        else:
            item.append(aValue)
    return item


print(flatten_dictionary2(example2))
