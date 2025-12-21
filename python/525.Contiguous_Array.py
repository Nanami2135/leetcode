from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count = 0
        distance = {}
        distance[0] = 0
        max = 0
        for i in range(0,len(nums),1):
            if nums[i] == 0:
                count -= 1
            elif nums[i] == 1:
                count += 1
            if count not in distance:
                distance[count] = i + 1
            elif count in distance:
                temp = i + 1 - distance[count]
                if temp > max :
                    max = temp
                
        return max


r = Solution()
assert r.findMaxLength([0,1]) == 2
assert r.findMaxLength([0,1,0]) == 2
assert r.findMaxLength([0,1,1,0,1,1,1,0]) == 4

print("Tests have passed.")