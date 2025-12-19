class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if int(num1)== 0 or int(num2) == 0:
            return "0"

        summa = 0

        if num1>=num2:
            bigger = num1
            smaller = num2
        else:
            bigger = num2
            smaller = num1
        
        number = 0

        for i in range(len(smaller)-1,-1,-1):
            digit = 1
            remainder = 0
            summa1 = 0
            
            for j in range(len(bigger)-1,-1,-1):

                sum = int(bigger[j]) * int(smaller[i]) + remainder
                remainder = sum//10
                summa1 = summa1 + digit * (sum%10) 
                digit *= 10
            summa1 = digit*remainder + summa1
            number += 1
            if number == 1:
                summa += summa1
            else:
                for i in range(number-1):
                    summa1 *= 10
                summa += summa1
        return str(summa)
        

                    

r = Solution()
assert r.multiply("42","10") == "420"
assert r.multiply("2","3") == "6"
assert r.multiply("123","456") == "56088"
print("Tests have passed.")  