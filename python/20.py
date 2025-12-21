from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = []
        zero_column = [] 

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i not in zero_row:

                        zero_row.append(i)
                    if j not in zero_column:
                        zero_column.append(j)

        for row in zero_row:
            for i in range(len(matrix[row])):
                matrix[row][i] = 0
        for column in zero_column:
            for i in range(len(matrix)):
                matrix[i][column] = 0

        return matrix
    

    # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if i in zero_row:
        #             matrix[i][j] = 0
        #         if j in zero_column:
        #             matrix[i][j] = 0
                

        


r = Solution()
assert r.setZeroes([[0,1]]) == [[0,0]]
assert r.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


print("Tests have passed.")
        