from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        test = 0
        result = 0
        l = 0

        steps = len(grid)

        # for i in range(len(grid)):
        #     for j in range(len(grid)):
        #         if grid[i][j] == grid[i][j]:
        #             test += 1
        #     if test == len(grid):
        #         result += 1
        #     test = 0
        
        row = grid
        column = []
        temp = []

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                temp.append(grid[j][i])
            column.append(temp)
            temp = []

        for n in row:
            if n in column:
                result += 1
        
        return result




        # l = 0
        # m = grid[0]
        # while l < len(grid) :

        #     for i in range(len(grid)):
        #         for j in range(len(grid)):
        #             if m[j] == grid[i][j]:
        #                 test += 1
        #             else:
        #                 break   
                      
        #         if test == len(grid):
        #             result += 1
        #         test = 0
        #     m = grid[i]
        #     l += 1

        return result
    
    



         
        # size = len(grid)
        # count = 0

        # m = 0

        # i = j = 0

        # for j in range(size):
        #     row = grid[j]
        #     for n in row:
        #         if grid[i][j] == row[j]:
        #             i += 1
        #             if i == size:
        #                 count += 1
        #                 i = 0
        #         else:
        #             i = 0
        #             continue
            
               


                
r = Solution()
assert r.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1
assert r.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
print("Tests have passed.") 

#   j
# i 0 1 2
# 0 3 2 1
# 1 1 7 6
# 2 2 7 7