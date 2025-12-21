from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        r = [0] * 1001

        for n in nums:
            r[n] += 1
        
        max_val = -1
        for i, n in enumerate(r):
            if r[i] == 1 and i > max_val:
                max_val = i

        return max_val
    
    
        
s = Solution()
assert s.largestUniqueNumber([5,7,3,9,4,9,8,3,1]) == 8
assert s.largestUniqueNumber([9,9,8,8]) == -1
