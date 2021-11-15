"""
You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

 

Example 1:

Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
Explanation:
- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
  The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
  The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
  Hence, the answer for them is the maximum beauty of all items, i.e., 6.
Example 2:

Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
Output: [4]
Explanation: 
The price of every item is equal to 1, so we choose the item with the maximum beauty 4. 
Note that multiple items can have the same price and/or beauty.  
Example 3:

Input: items = [[10,1000]], queries = [5]
Output: [0]
Explanation:
No item has a price less than or equal to 5, so no item can be chosen.
Hence, the answer to the query is 0.
"""

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        """
        [[1,2],[3,2],[2,4],[5,6],[3,5]]
           ^
        [1,2,3,4,5,6]
         ^
        Output    
        [2,4,5,5,6,6]
        
         [[1,2],[1,2],[1,3],[2,4],[5,5]], queries = [3,6]
         1:3, 2:4, 5:6
        """
        items.sort()
        N = len(queries)
        new = [(v,i) for i,v in enumerate(queries)]
        new.sort()
        ans = [0] * N
        score = j = 0
		# we iterate through items from the lowest to the highest and update current max number
		# if the price in queries is higher, we add current max to answer at corresponding index
        for k,v in items:
            while j < N and k > new[j][0]:
                ans[new[j][1]] = score
                j += 1
            score = max(score, v)
			
		# if there are bigger prices in queries than available in items, we put max number
        while j < N:
            _, idx = new[j]
            ans[idx] = score
            j += 1
        return ans
        
        
        
#         Passed 31/35 test cases
#         myDict = {}
#         myList = []
#         res = []
#         for i in range(len(items)):
#             myDict[items[i][0]]=items[i][1]
#             myList.append(items[i][0])
        
#         for i in queries:
#             # Edge cases
#             if i < min(myList): res.append(0)
#             # if the number is within the range
#             else:
#                 temp = []
#                 for aKey, aValue in myDict.items():
#                     if i-aKey>=0:
#                         temp.append(aValue)
#                 res.append(max(temp))
#         return res
                
                
                
            