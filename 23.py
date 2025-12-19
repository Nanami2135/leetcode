from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        bill_5 = 0
        bill_10 = 0
        bill_20 = 0

        lemonade = 5

        # banknots = [10,5]

        for customer in bills:
            if customer == 5:
                bill_5 += 1
            if customer == 10:
                if bill_5 - 1 < 0:
                    return False
                bill_10 += 1
                bill_5 -= 1
            if customer == 20:
                if bill_10 - 1 < 0:
                    if bill_5 - 3 < 0:
                        return False
                    bill_5 -= 3  
                else:
                    if bill_5 - 1 < 0:
                        return False
                    bill_10 -= 1 
                    bill_5 -= 1
        return True 

        # for castomer in bills:
        #     if castomer == 5:
        #         bill_5 += 1
        #     else:
        #         change = castomer - lemonade
        #         for banknote in banknots:
        #             ban
    
        

r = Solution()
assert r.lemonadeChange([5,5,5,5,20,20,5,5,20,5]) == False
assert r.lemonadeChange([5,5,10,10,20]) == False
print("Tests have passed.")  