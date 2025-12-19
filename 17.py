from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        sum_richest = 0
        sum_wealth = 0
        for i in range(len(accounts)):
             for j in range(len(accounts[i])):
                sum_wealth += accounts[i][j]
                if j == len(accounts[i]) - 1:
                    if sum_wealth > sum_richest:
                        sum_richest = sum_wealth
                    sum_wealth = 0
                    
        return sum_richest

        

r = Solution()
# assert r.maximumWealth([[1,2,3],[3,2,1]]) == 6
assert r.maximumWealth([[1,5],[7,3],[3,5]]) == 10
assert r.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17

print("Tests have passed.")