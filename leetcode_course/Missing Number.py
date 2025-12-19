from collections import defaultdict
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        our_nums = set(nums)
        n = len(our_nums)      
        for i in range(0,n+1,1):
            if i not in our_nums:
                return i
            

r = Solution()
assert r.missingNumber([3,0,1]) == 2
assert r.missingNumber([0,1]) == 2
assert r.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
print("Tests have passed.")