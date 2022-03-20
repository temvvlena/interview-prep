'''
Python program to design a DS that
supports following operations
in Theta(n) time:
a) Insert
b) Delete
c) Search
d) getRandom
'''
import random

myList = []
myHash = {}

def insert(num):

    # If element is already present,
    # then nothing has to be done
    if num in myHash:
        return

    # Else put element at
    # the end of the list
    s = len(myList)
    myList.append(num)

    # Also put it into hash
    myHash[num] = s

# A Theta(1) function to remove an element
# from MyDS data structure
def remove(num):

    # Check if element is present
    indenum = myHash.get(num, None)
    if indenum == None:
        return

    # If present, then remove
    # element from hash
    del myHash[num]

    # Swap element with last element
    # so that removal from the list
    # can be done in O(1) time
    size = len(myList)
    last = myList[size - 1]
    myList[indenum], myList[size - 1] = myList[size - 1], myList[indenum]

    # Remove last element (This is O(1))
    del myList[-1]

    # Update hash table for
    # new indenum of last element
    myHash[last] = indenum

# Returns a random element from MyDS
def getRandom():
    # Find a random indenum from 0 to size - 1
    indenum = random.randrange(0, len(myList))

    # Return element at randomly picked indenum
    return myList[indenum]

# Returns indenum of element
# if element is present,
# otherwise none
def search(num):
    return myHash.get(num, None)

# Driver Code

insert(10)
insert(20)
insert(30)
insert(40)
print(search(30))
remove(20)
insert(50)
print(search(50))
print(getRandom())