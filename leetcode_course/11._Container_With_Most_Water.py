from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        
        result = 0
        l = len(height) - 1

        i = 0
        j = len(height) - 1

        while i != j:
            if height[i] > height[j]:
                temp_height = height[j]
                max_water = temp_height * l
                result = max(result,max_water)
                j -= 1
            else:
                temp_height = height[i]
                max_water = temp_height * l 
                result = max(result,max_water)
                i += 1
            l -= 1

        return result


r = Solution()
assert r.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert r.maxArea([1,1]) == 1


print("Tests have passed.")
        