"""
https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/
1868. Product of Two Run-Length Encoded Arrays
"""


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        product_encoded = []

        e1_index = 0
        e2_index = 0

        while e1_index < len(encoded1) and e2_index < len(encoded2):
            e1_val, e1_freq = encoded1[e1_index]
            e2_val, e2_freq = encoded2[e2_index]

            product_val = e1_val * e2_val
            product_freq = min(e1_freq, e2_freq)

            encoded1[e1_index][1] -= product_freq
            encoded2[e2_index][1] -= product_freq

            if encoded1[e1_index][1] == 0:
                e1_index += 1

            if encoded2[e2_index][1] == 0:
                e2_index += 1

            if not product_encoded or product_encoded[-1][0] != product_val:
                product_encoded.append([product_val, product_freq])
            else:
                product_encoded[-1][1] += product_freq

        return product_encoded
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
