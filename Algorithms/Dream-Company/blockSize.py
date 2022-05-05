"""
Given a list of transactions in format (id, fee, size) and a blockSize, choose a subset of them so that they fit with
blockSize and fee is maximized. A greedy solution was ok although it might not be most optimal. Coded up the greedy
solution using heap - had to fix a few bugs when we ran it. Was asked a followup - the transactions can now have
parent-child relationships, i.e for a child transaction to complete a parent transaction must be completed first.
Talked about how we can modify the greedy solution to handle this and coded it up. He ran it against a new test case
and it worked well but pointed out a flaw in the logic which would give an incorrect result for certain cases.
I acknowledged the flaw and discussed with him how it can be fixed.
"""


class BlockSize:
    def __init__(self, t, blockSize):
        self.transactions = t
        self.blockSize = blockSize

    def getMaximumFee(self):
        feeOverSize = [(i, fee, size, fee / size) for i, fee, size in self.transactions]
        feeOverSize.sort(key=lambda x: x[3], reverse=True)
        knapsack = [0] * len(self.transactions)
        for i, f, s, fs in feeOverSize:
            if self.blockSize > s:
                self.blockSize -= s
                knapsack[i - 1] = 1
            elif self.blockSize > 0:
                knapsack[i - 1] = self.blockSize / s
                self.blockSize = 0
        totalProfit, totalWeight = 0, 0
        for i in range(len(feeOverSize)):
            totalProfit += feeOverSize[i][1] * knapsack[feeOverSize[i][0] - 1]
            totalWeight += feeOverSize[i][2] * knapsack[feeOverSize[i][0] - 1]
        print(totalProfit, totalWeight)


t = [(1, 10, 2), (2, 5, 3), (3, 15, 5), (4, 7, 7), (5, 6, 1), (6, 18, 4), (7, 3, 1)]
blockSize = 15
a = BlockSize(t, blockSize)
a.getMaximumFee()
