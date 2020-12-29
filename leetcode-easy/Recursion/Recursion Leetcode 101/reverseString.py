# Print a string in reverse order.
def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 

def printReverse(s):
    helper(0, s)
def helper(myIndex, myChar):
    if myIndex >= len(myChar):
        return
    helper(myIndex + 1, myChar)
    print(myChar[myIndex])
print(printReverse("abc"))