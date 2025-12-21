from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        len_matrix = len(matrix)*len(matrix[0])
        result = []
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                result.append(matrix[i][0])
            return result

        while len(result) != len_matrix:
            row = len(matrix)
            column = len(matrix[0])
            start = 1
            for i in range(row):
                if i == 0:
                    for j in range(column):
                        result.append(matrix[i][j])
                elif i == row - 1:
                    for j in range(column - 1,-1,-1):
                        if i != row - 1:
                            result.append(matrix[i][0])
                            
                        else:
                            result.append(matrix[i][j])
                    if len(result) == len_matrix:
                        break
                    for i in range(row - 2,0,-1):
                        
                        result.append(matrix[i][0])
                    # if len(result) == len_matrix:
                    #             break
    
                    matrix = matrix[start:row-1]
                    for i in range(len(matrix)):
                        matrix[i].pop(0)
                        matrix[i].pop(len(matrix[i])-1)
                             
                    break
                elif i != 0 and len(result)>=column<=column+row:
                    result.append(matrix[i][column-1])

        return result
               


r = Solution()
# assert r.spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]) == [7,9,6]
assert r.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
assert r.spiralOrder([[5]]) == [5]

print("Tests have passed.")