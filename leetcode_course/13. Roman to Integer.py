class Solution:
    def romanToInt(self, s: str) -> int:

        romanNumbers = {"I": 1, "V": 5, "X" : 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        temp = 0

        for i in range(len(s)-1,-1,-1):
            n = romanNumbers[s[i]]
            if n>= temp:
                res += n
            else:
                res -= n
            temp = n

        return res



r = Solution()
assert r.romanToInt("III") == 3
assert r.romanToInt("LVIII") == 58
assert r.romanToInt("MCMXCIV") == 1994

print("Tests have passed.")