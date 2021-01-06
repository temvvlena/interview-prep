"""
https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

"""
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
    # Store min value and x as a list of lists in items
    def push(self, x):
        if len(self.items) == 0:
            self.items.append([x, x])
        else:
            self.items.append([x, min(x, self.getMin())])

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[-1][0]

    def getMin(self):
        return self.items[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()