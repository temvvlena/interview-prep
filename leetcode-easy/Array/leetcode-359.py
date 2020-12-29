
# https://leetcode.com/problems/logger-rate-limiter/
# Time Complexity: O(1). The lookup and update of the hashtable takes a constant time.

# Space Complexity: O(M) where MM is the size of all incoming messages. 
# Over the time, the hashtable would have an entry for each unique message that has appeared.
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if (message not in self.messages) or (timestamp - self.messages[message] >= 10):
            self.messages[message] = timestamp
            return True
        return False
    