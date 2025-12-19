class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100 ,"D" : 500,"M" : 1000}
        result = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                result += symbols[s[i]]
            elif symbols[s[i]] >= symbols[s[i+1]]:
                result += symbols[s[i]]
            else:
                result += symbols[s[i+1]] - symbols[s[i]]
                i += 1
            i += 1

        return result

    
# M = 1000, CM = 900, XC = 90 and IV = 4.
            
r = Solution()
assert r.romanToInt("MCMXCIV") == 1994
assert r.romanToInt("III") == 3
assert r.romanToInt("LVIII") == 58
assert r.romanToInt("MDCCXIV") == 1714

print("Tests have passed.")
