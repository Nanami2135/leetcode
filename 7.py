class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        digits[i] += 1
        if digits[i] == 10:
            while i != 0:
                digits[i] = 0
                digits[i-1] += 1
                if digits[i - 1] != 10:
                    break
                i -= 1
        
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        
        return digits

        # i = len(digits)-1
        # digits[i] = (digits[i] + 1) % 10
        # if digits[i] == 0:
        #     while i != 0:
        #         digits[i-1] = (digits[i-1] + 1) % 10
        #         if digits[i - 1] != 0:
        #             break
        #         i -= 1
        
        # if digits[0] == 0:
        #     return [1] + digits
        
        # return digits

r = Solution()
assert r.plusOne([4,3,2,1]) == [4,3,2,2]
assert r.plusOne([1,3,4,8,9]) == [1,3,4,9,0]
assert r.plusOne([9,9,9]) == [1,0,0,0]

