class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            if low%2 != 0:
                return 1
            else:
                return 0
        if low == 0 and high%2 != 0:
            return high//2 + 1
        if low == 0 and high%2 == 0:
            return high//2 
        if low%2 == 0 and high%2 == 0:
            return (high - low)//2
        if low%2 != 0 or high %2 != 0:
            return (high - low)//2 + 1

        






r = Solution()
assert r.countOdds(21,22) == 1
assert r.countOdds(8,10) == 1

print("Tests have passed.")  