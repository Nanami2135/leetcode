from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return len(nums)

        new_nums = set(nums)
        count = 1
        result = 0
        # while len(new_nums) != 0:
        for n in nums:
            if len(new_nums) == 0:
                break
            if n not in new_nums:
                continue
            new_nums.remove(n)
            if n + 1 in new_nums and n - 1 in new_nums:
                maximum = n + 1
                min = n - 1
                while maximum in new_nums and min in new_nums:
                    count += 2
                    new_nums.remove(maximum)
                    new_nums.remove(min)
                    maximum += 1
                    min -= 1
                while maximum in new_nums:
                    count += 1
                    new_nums.remove(maximum)
                    maximum += 1
                while min in new_nums:
                    count += 1
                    new_nums.remove(min)
                    maximum -= 1
                result = max(result, count)
                count = 0
            elif n + 1 in new_nums:
                maximum = n + 1
                while maximum in new_nums:
                    count += 1
                    new_nums.remove(maximum)
                    maximum += 1
                result = max(result, count)
                count = 0
            elif n - 1 in new_nums:
                min = n - 1
                while min in new_nums:
                    count += 1
                    new_nums.remove(min)
                    min -= 1
                result = max(result, count)
                count = 0
            
            result = max(result, count)
            count = 1

        return result


                
                    



r = Solution()
assert r.longestConsecutive([-2,-3,-3,7,-3,0,5,0,-8,-4,-1,2]) == 5

assert r.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
assert r.longestConsecutive([-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7]) == 4
assert r.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
assert r.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]) == 7


print("Tests have passed.")