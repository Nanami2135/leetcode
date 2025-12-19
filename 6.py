class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        i = 0
        j = 1

        # while j != len(nums):
        #     if nums[i] == 0 and nums[j] == 0:
        #         j += 1
        #     elif nums[i] == 0:
        #         nums[i] = nums[j]
        #         nums[j] = 0
        #         i += 1
        #         j += 1
        #     else:
        #         i += 1
        #         j += 1

        while j != len(nums):
            if nums[i] == 0 and nums[j] == 0:
                j += 1
                continue
            elif nums[i] == 0:
                nums[i] = nums[j]
                nums[j] = 0
            i += 1
            j += 1
                
        return nums


r = Solution()
assert r.moveZeroes([0,2,6,0,0,7,0]) == [2,6,7,0,0,0,0]
assert r.moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
assert r.moveZeroes([1,0]) == [1,0]

print("Tests have passed.")
l = [0,2,6,0,0,7,0]
one = [1,2,5]
zero = [0,3,4,6]



