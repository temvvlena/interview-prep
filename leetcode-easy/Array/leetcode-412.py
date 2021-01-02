"""
https://leetcode.com/problems/fizz-buzz/
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” 
instead of the number and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.
Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
class Solution:
    def fizzBuzz(self, n):
        # 45 / 3 * 5 == 4 + 5 = 9 
        # FindDivisibility
        # 1 % 3 = 1
        # 2 % 3 = 2
        # 3 % 3 = 0
        # 4 % 3 = 1
        # 45 % 3 = 0
        # 45 % 5 = 0
        # 45 % 
        # 15 
        #{3: Fizz, 4: Bam, 5: Buzz, 6: Bash, 7: Fuzz, 8: Fazz, 9: Fezz}
        myList = []
        for i in range(1, n+1):
            if i % 15 == 0:
                myList.append("FizzBuzz")  
            elif i % 3 == 0:
                myList.append("Fizz")
            elif i % 5 == 0:
                myList.append("Buzz")
            else:
                myList.append(str(i))
        return myList
        """
        # More Dynamic
        myList = []
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
        for i in range(1, n+1):
            num_ans_str = ""
            for key in fizz_buzz_dict.keys():
                if i % key == 0:
                    num_ans_str += fizz_buzz_dict[key]
            if not num_ans_str:
                num_ans_str = str(i)
            
            myList.append(num_ans_str)
        return myList
        """
        
