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
        
        def backtrack(first = 0):
            if first == n:
                # Append the copy of the list
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                # Here's the backtracking algorithm works
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        output = []
        backtrack()
        return output