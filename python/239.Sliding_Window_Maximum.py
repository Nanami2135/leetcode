from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = 0
        n = k
        max = [[0,0]]
        result = []
        while n != len(nums)+1:
            slide = nums[m:n]
            j = 0
            for i in slide:
                temp = max[-1]
                if i >= temp[1]:
                    max.append([j,i])
                j += 1
            m += 1
            n += 1
            result.append(max[-1])
            max = [[0,0]]
        
        return result

                





r = Solution()
assert r.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
assert r.maxSlidingWindow([1], 1) == [1]
# assert r.maxSlidingWindow("s") == "s"

print("Tests have passed.")