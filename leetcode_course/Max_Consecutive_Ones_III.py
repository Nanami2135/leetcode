from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = 0
        curr = 0
        s = k
        i = 0
        j = 0
        while True:
            if j == len(nums) - 1:
                if nums[j] == 1:
                    curr += 1
                    length = max(length, curr)
                    break
                else:
            
                    length = max(length, curr)
                    break 
            elif nums[j] == 1:
                j += 1
                curr += 1
            elif nums[j] == 0:
                if s != 0:
                    j += 1
                    s -= 1
                    curr += 1
                else:
                    while nums[i] != 0:
                        i += 1
                    i += 1
                    s = k
                    j = i
                    length = max(length, curr)
                    curr = 0

        return length
            
        

r = Solution()
assert r.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
assert r.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3) == 10
print("Tests have passed.") 