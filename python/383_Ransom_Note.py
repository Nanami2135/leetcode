class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dict_mag = {}

        for symbol in magazine:
            if symbol not in dict_mag:
                dict_mag[symbol] = 1
            else:
                dict_mag[symbol] += 1

        for symbol in ransomNote:
            if symbol in dict_mag and dict_mag[symbol] != 0:
                dict_mag[symbol] -= 1
            else:
                return False
        
        return True


r = Solution()
assert r.canConstruct("a", "b") == False
assert r.canConstruct("aa", "ab") == False
assert r.canConstruct("aa", "aab") == True


print("Tests have passed.")