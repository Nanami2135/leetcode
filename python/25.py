class Solution(object):
    def tangenc(self, p1, p2):
        opposite = p2[1] - p1[1]
        adjacent = p2[0] - p1[0]
        if adjacent == 0:
            return None
        return opposite/adjacent
         
        
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """

        tan = self.tangenc(coordinates[0], coordinates[1]) 

        for i in range(1,len(coordinates) -1):

            if self.tangenc(coordinates[i], coordinates[i + 1]) != tan:
                return False
            
        return True
    
        # a = (coordinates[1][0] - coordinates[0][0])
        # b = (coordinates[1][1] - coordinates[0][1])
        # gepot_2 = a * a + b * b
        # gepot = gepot_2**(0.5) 
        # cos = a/gepot
        
        # for i in range(2,len(coordinates),1):
        #     if (coordinates[i][0] - coordinates[i-1][0])/(coordinates[i][0] - coordinates[i-1][0]) != tang:
        #         return False
            
        # return True


        

r = Solution()
assert r.checkStraightLine([[0,0],[0,1],[0,-1]]) == True
assert r.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False
print("Tests have passed.")  