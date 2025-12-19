class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        pos_or_neg = 0
        for x,y in zip(nums, nums[1:]):
            if y > x:
                if pos_or_neg == 0:
                    pos_or_neg = 1
                if pos_or_neg == -1:
                    return False
            elif y < x:
                if pos_or_neg == 0:
                    pos_or_neg = -1
                if pos_or_neg == 1:
                    return False
        
        return True



a = [5,5,5,3,2]
b = [0,3,2]

c = Solution()
r = c.isMonotonic(b)
print(r)


# r = Solution.isMonotonic(c, a)


# print (list(zip(a,b)))

# 1,2,3,4,5,5
#  1,2,3,4,5,6