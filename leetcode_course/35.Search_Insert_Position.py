from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 0

        for i in range(0,len(nums)):
            if target == nums[i]:
                return i
            elif i == len(nums) - 1:
                return len(nums)
            elif target > nums[i] and target < nums[i +1]:
                return i + 1
         

        


r = Solution()
assert r.searchInsert([1,3,5,6],5) == 2
assert r.searchInsert([1,3,5,6],2) == 1
assert r.searchInsert([1,3,5,6],7) == 4

print("Tests have passed.")