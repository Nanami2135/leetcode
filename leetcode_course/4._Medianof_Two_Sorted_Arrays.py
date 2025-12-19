from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        l = len(nums1) + len(nums2)
        result = 0

        if l%2 == 0:
            mediana = [l/2,l/2 - 1]
        else:
            mediana = [l//2]
        
        i = 0
        j = 0
        count = 0
        
        while len(mediana) != 0 and count != l:
            if i != len(nums1) and j != len(nums2):
                if nums1[i] < nums2[j]:
                    if count == mediana[-1]:
                        result += nums1[i]
                        mediana.pop()
                    i += 1
                elif nums1[i] > nums2[j]:
                    if count == mediana[-1]:
                        result += nums2[j]
                        mediana.pop()
                    j += 1
                elif nums1[i] == nums2[j]:
                    if len(mediana) == 2 and count == mediana[-1]:
                        result = nums1[i] + nums2[j]
                        return result/2
                    i += 1
                    j +=1
                    count += 1
            elif i != len(nums1) and j == len(nums2):
                if count == mediana[-1]:
                    result += nums1[i]
                    mediana.pop()
                i += 1
            elif i == len(nums1) and j != len(nums2):
                if count == mediana[-1]:
                    result += nums2[j]
                    mediana.pop()
                j += 1
                
            count += 1
            # if count > l
        
        if l%2 == 0:
            return result/2
        else:
            return result
   


            
            



        # if l%2 != 0:
        #     mediana = int(l/2)
        #     if mediana > len(nums1):
        #         mediana -= len(nums1)
        #         return float(nums2[mediana])
        #     if mediana < len(nums1):
        #         return float(nums1[mediana]) 
        # else:
        #     mediana = int(l/2)
        #     a = mediana - 1
        #     b = mediana
        #     if a < len(nums1):
        #         a = nums1[a]
        #     else:
        #         a -= len(nums2)
        #         a = nums2[a]
        #     if b < len(nums1):
        #         b =nums1[b]
        #     else: 
        #         b -= len(nums2)
        #         b = nums2[b]
            
        #     result = a + b
        #     return result / 2



    

r = Solution()
assert r.findMedianSortedArrays([0,0],[0,0]) == 0
assert r.findMedianSortedArrays([1,2],[3]) == 2.00000
assert r.findMedianSortedArrays([1,2],[3,4]) == 2.50000
assert r.findMedianSortedArrays([2,2,4,4],[2,2,2,4,4]) == 2.00000

# [1,2,3,4,5,6,7],[8,9,10,11,12,13,14,15,16,17,18,19]


print("Tests have passed.")