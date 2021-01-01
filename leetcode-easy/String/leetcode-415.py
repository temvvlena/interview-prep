class Solution:
    def addStrings(self, num1, num2):
        
        hashMap = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        s1, s2 = 0, 0
        for c in num1:
            s1 = s1 * 10 + hashMap[c]
        for c in num2:
            s2 = s2 * 10 + hashMap[c]
        return (str(s1+s2))
        
     