"""
insert(x): Inserts an item x to the data structure if not already present.
remove(x): Removes item x from the data structure if present.
search(x): Searches an item x in the data structure.
getRandom(): Returns a random element from current set of elements
"""
import random

myNums = []
myHash = {}

def insert(num):
    if isinstance(search(num), int):
        return
    else:
        myNums.append(num)
        myHash[num] = len(myNums)-1

def remove(num):
    if search(num) is None: return
    else:
        indexOfHashMapRemoved = myHash[num]
        del myHash[num]
        if indexOfHashMapRemoved == len(myNums)-1:
            myNums.pop()
        else:
            myNums[indexOfHashMapRemoved], myNums[-1] = myNums[-1], myNums[indexOfHashMapRemoved]
            myNums.pop()
            myHash[myNums[indexOfHashMapRemoved]] = indexOfHashMapRemoved

def search(num):
    return myHash.get(num, None)

def getRandom():
    return myNums[random.randint(1, 10**4) % len(myNums)]

insert(30)
insert(30)
insert(30)
insert(1)
insert(2)
insert(3)
insert(4)
insert(47)
insert(53)
insert(444)
insert(4444)
insert(54443)
remove(30)
remove(30)
remove(30)
remove(30)
remove(47)
remove(47)
remove(47)
remove(444)
remove(54443)
print(getRandom())
print(getRandom())
print(getRandom())
print(getRandom())
print(getRandom())
print(getRandom())
print(getRandom())
print(getRandom())
print(getRandom())