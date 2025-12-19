from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix_sum = nums[0]
        prev_sum = nums[0]

        for i in range(1, len(nums)):
            new_sum = prev_sum + nums[i]
            
            if min_prefix_sum > new_sum:
                min_prefix_sum = new_sum
            
            prev_sum += nums[i]
            
        if min_prefix_sum > 0:
            return 1
        else:
            return abs(min_prefix_sum) + 1


r = Solution()
assert r.minStartValue([-3,2,-3,4,2]) == 5
assert r.minStartValue([-5,-2,4,4,-2]) == 8
assert r.minStartValue([1,2]) == 1
assert r.minStartValue([1,-2,-3]) == 5
print("Tests have passed.") 

# -3, 1, -2, 2, 4