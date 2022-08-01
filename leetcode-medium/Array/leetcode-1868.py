"""
https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/
1868. Product of Two Run-Length Encoded Arrays
"""


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        e1_index, e2_index = 0, 0
        res = []
        while e1_index < len(encoded1) and e2_index < len(encoded2):
            e1_val, e1_freq = encoded1[e1_index]
            e2_val, e2_freq = encoded2[e2_index]

            product = e1_val * e2_val

            min_freq = min(e1_freq, e2_freq)

            if not res or product != res[-1][0]:
                res.append([product, min_freq])
            else:
                res[-1][1] += min_freq

            encoded1[e1_index][1] -= min_freq
            encoded2[e2_index][1] -= min_freq

            if e1_freq == 0:
                e1_index += 1
            if e2_freq == 0:
                e2_index += 1
        return res
        """
        Time Limit Exceeded
        def decodeArray(anArray):
            decodedArray = []
            for index, value in anArray:
                for num in range(value):
                    decodedArray.append(index)
            return decodedArray
        decode1 = decodeArray(encoded1)
        decode2 = decodeArray(encoded2)
        productArray = []
        i = 0 
        while i < len(decode1):
            productArray.append(decode1[i]*decode2[i])
            i += 1
        i = 0
        res = []
        stack = []
        while i < len(productArray):
            if len(stack) == 0:
                stack.append(productArray[i])
            elif productArray[i] not in stack:
                res.append([stack[0], len(stack)])
                stack = []
                stack.append(productArray[i])
            else:
                stack.append(productArray[i])
            i += 1
        if stack:
            res.append([stack[0], len(stack)])
        return res
        """
