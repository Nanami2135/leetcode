from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0

        i = 0
        j = 0
        to_flip = k

        while j != len(nums) and i != len(nums):
            if nums[i] == 0:
                if to_flip == 0:
                    i += 1
                    1
                    continue
                to_flip -= 1
            
            while True:
                j += 1
                if j == len(nums):
                    j -= 1
                    break

                if nums[j] == 0:
                    if to_flip == 0:
                        j -= 1
                        break

                    to_flip -= 1
            
            max_len = max(max_len, j - i + 1)

            if nums[i] == 0:
                to_flip += 1
            i += 1
            if j <= i:
                j = i
                to_flip = k

        print(max_len)
        return max_len


r = Solution()
# assert r.longestOnes([0,1,0,1], 1) == 3
# assert r.longestOnes([0,0,0], 1) == 1
# assert r.longestOnes([0,0,0], 0) == 0
# assert r.longestOnes([1,1,1], 0) == 3
# assert r.longestOnes([1,1,1], 3) == 3
# assert r.longestOnes([1,0,0,1,1,0], 1) == 3

assert r.longestOnes([1,0,0,0,1,1,0], 2) == 4

# assert r.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
# assert r.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3) == 10
print("Tests have passed.")
