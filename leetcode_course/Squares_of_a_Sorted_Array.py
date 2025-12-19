from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        while True:
            if i == j:
                result[k] = nums[j] ** 2
                break

            if abs(nums[i]) > abs(nums[j]):
                result[k] = nums[i] ** 2
                i += 1
            else:
                result[k] = nums[j] ** 2
                j -= 1
            k -=1
            
        return result
            


# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].



r = Solution()
assert r.sortedSquares([-5,-3,-2,-1]) == [1,4,9,25]
assert r.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
print("Tests have passed.") 