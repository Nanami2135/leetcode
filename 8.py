class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negative = 0
        for number in nums:
            if number > 0:
                continue
            if number < 0:
                negative += 1
            if number == 0:
                return 0
                    
        if negative % 2 == 0:
            return 1
        else:
            return -1
             
    def signFunc(self, x):
        """
        :type x: int
        :rtype: int
        """   
        return x
                 
          
