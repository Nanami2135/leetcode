from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if b + c > a:
                return a + b + c
        
        return 0


        




r = Solution()
assert r.largestPerimeter([2,1,2]) == 5
assert r.largestPerimeter([1,2,1,10]) == 0
print("Tests have passed.")  
        