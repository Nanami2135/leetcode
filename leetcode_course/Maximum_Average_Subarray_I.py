from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_summ = sum(nums[0:k])
        curr = max_summ
        left = 1
        right = k
    
        while right != len(nums):
            
            curr = curr - nums[left - 1] + nums[right]
            max_summ = max(max_summ,curr)
            left += 1
            right += 1

        return max_summ/k

        


r = Solution()
assert r.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75000
assert r.findMaxAverage([0,4,0,3,2],1) == 4
print("Tests have passed.") 



        