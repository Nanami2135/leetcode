from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return (len(nums))

        n = 1
        i = 0
        j = 1
        while j != len(nums):
            if  nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
                n += 1

        return (n)
    
r = Solution()
assert r.removeDuplicates([1,1,2]) == 2
assert r.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
# assert r.maxSlidingWindow("s") == "s"

print("Tests have passed.")

        
        