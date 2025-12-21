from collections import defaultdict
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums_dict = defaultdict(int)
        result = []

        for i in range(len(nums2)):
            nums_dict[nums2[i]] = i

        for i in range(len(nums1)):
            position = nums_dict[nums1[i]]
            if position + 1 == len(nums2):
                result.append(-1)
            else:
                next_position = position + 1
                while True:
                    if next_position == len(nums2):
                        result.append(-1)
                        break
                    elif nums2[next_position] > nums1[i]:
                        result.append(nums2[next_position])
                        break
                    else: 
                        next_position += 1
        
        return result


r = Solution()
assert r.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]) == [7,7,7,7,7]
assert r.nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]

print("Tests have passed.")