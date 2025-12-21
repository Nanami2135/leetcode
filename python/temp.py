from typing import List, Dict, Any


class Solution:
    def findFib(self, nums: int) -> List[int]:

        # prev = 0
        # fib = [0,1]

        # for i in range(nums):
        #         curr = prev + fib[-1]
        #         prev = fib[-1]
        #         fib.append(curr)
        
        # print (fib)
        # # return fib

        def findFibRecur(curr: int, prev: int) -> List[int]:
            s =[]
             
            new_curr = curr + prev
            prev = curr
            curr = new_curr
            s.append(curr, prev)
            return s
        
        print ( m = findFibRecur(8,5))
        return m



    
    


                


        

 

    
r = Solution()
assert r.findFib(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# assert r.findMaxLength([0,1,0]) == 2
# assert r.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
print("Tests have passed.")