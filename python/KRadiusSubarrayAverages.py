from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if len(nums) < k:
            result = [-1] * len(nums)
            return result 
        
        i = 0
        j = k * 2
        num_in_avg = ((k*2) + 1)
        result = [-1] * len(nums)
        d = sum(nums[i:j + 1]) 
        result[k] = d // num_in_avg
        m = k + 1

        while j != len(nums) - 1:
            i += 1
            j += 1
            d = (d - nums[i-1] + nums[j]) 
            result[m] = d // ((k*2) + 1)
            m += 1
        
        return result








        # result_nums = [nums[0]]
        # for i in range(1,len(nums)):
        #     result_nums.append(nums[i] + result_nums[-1])

        # if len(nums) < k:
        #     result = [-1] * len(nums)
        #     return result 
        # i = 0
        # j = k * 2
        # result = [-1] * k
        # while j< len(nums):
        #     m = result_nums[j] - result_nums[i] + nums[i]
        #     m = m // ((k * 2) + 1)
        #     result.append(m)
        #     i += 1
        #     j += 1
        # k = len(nums) - len(result)
        # result = result + [-1] * k
        # return result
    
        # result_nums = [nums[0]]
        # for i in range(1,len(nums)):
        #     result_nums.append(nums[i] + result_nums[-1])












r = Solution()
assert r.getAverages([7,4,3,9,1,8,5,2,6], 3) == [-1,-1,-1,5,4,4,-1,-1,-1]
# assert r.getAverages([9], ) == [100000]
print("Tests have passed.") 