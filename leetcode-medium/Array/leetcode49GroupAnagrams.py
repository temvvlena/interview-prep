class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # In this problem, since the length of an array is within 0 --> 100, so it's better to sort strings and then compare them
        
        """
        Solution 2
        """
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    
        # Solution 1
        # Time complexity N*KLogN
        # Space complexity N*K
        #Sort it first
        #then add 
        """
        myHash = {}
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in myHash: myHash[temp]=[i]
            else: myHash[temp].append(i)
        res = []
        for aValue in myHash.values():
            temp = []
            for j in aValue: temp.append(strs[j])
            res.append(temp)       
        return res
        """