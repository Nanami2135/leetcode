class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        d_ran = {}
        d_mag = {}

        for i in range(len(magazine)):
            r = magazine[i]
            if r not in d_mag:
                d_mag[r] = 1
            else:
                d_mag[r] += 1
            if i < len(ransomNote):
                r = ransomNote[i]
                if r not in d_ran:
                    d_ran[r] = 1
                else:
                    d_ran[r] += 1

        for key in d_ran:
            if key not in d_mag or d_ran[key] > d_mag[key]:
                return False
            
        return True
            

                
r = Solution()
assert r.canConstruct("a","b") == False
assert r.canConstruct("aa","ab") == False
assert r.canConstruct("aa","aab") == True

print("Tests have passed.")