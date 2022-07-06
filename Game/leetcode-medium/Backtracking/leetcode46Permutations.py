class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        [1, 2, 3]
        
--------------------------------------------------
first = 0
      i = 0                     i = 1                i = 2
        |                         |                    |
     1, 2, 3                    2, 1, 3              3, 2, 1
    
--------------------------------------------------
first = 1                   
     /  \
  i = 1  i = 2
    |         |
  1, 2, 3   1, 3, 2             2, 1, 3  2, 3, 1      3, 1, 2  3, 2, 1
----------------------------------------------------
first = 2                       
     |
   1, 3, 2    
    
   [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]     
        """

        """
        https://leetcode.com/problems/permutations/
        46. Permutations
        """


class Solution:
    def permute(self, nums=):
        def backtrack(first=0):
            if first == length:
                output.append(nums[:])
            for i in range(first, length):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        output = []
        length = len(nums)
        backtrack()
        return output
