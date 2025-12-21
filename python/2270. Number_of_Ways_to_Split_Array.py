from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        ind_sum = [nums[0]]
        for i in range(1,len(nums)):
            ind_sum.append(nums[i] + ind_sum[len(ind_sum)-1])

        result = 0

        for i in range(0,len(nums) - 1):
            if ind_sum[i] >= ind_sum[len(ind_sum) - 1] - ind_sum[i + 1] + nums[i + 1]:
                result += 1
        
        return result

# 10,14,6,13

r = Solution()
assert r.waysToSplitArray([10,4,-8,7]) == 2
assert r.waysToSplitArray([2,3,1,0]) == 2
print("Tests have passed.") 