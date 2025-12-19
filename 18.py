from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        sum_diag = 0
        
        for i in range(n):
            sum_diag += mat[i][i] + mat[i][n - i - 1]
            
        
        if n % 2 != 0:
            sum_diag -= mat[n // 2][n // 2]
        
        return sum_diag 


r = Solution()
assert r.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]) == 25
assert r.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 8
assert r.diagonalSum([[5]]) == 5

print("Tests have passed.")