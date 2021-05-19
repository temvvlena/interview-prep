class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # hervee s2 empty bish bol shuud pop hiine
        # s1 dehi buh number s2 shiljuuleh ystoi, tegsniihee daraa hamgiin deed talin element avna
        # s1 = empty
        
        # 1, 2, 3
        if len(self.s2) > 0: return self.s2.pop()
        else:
            self.helper(self.s1)
            return self.s2.pop()
    
    def helper(self, myList): 
        while myList: self.s2.append(myList.pop())
    
    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.s2) > 0: return self.s2[-1]
        else:
            self.helper(self.s1)
            return self.s2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (len(self.s1) > 0 or len(self.s2) > 0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()