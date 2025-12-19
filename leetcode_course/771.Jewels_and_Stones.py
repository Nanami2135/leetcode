class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        d_stones = {}
        for n in stones:
            if n not in d_stones:
                d_stones[n] = 1
            else:
                d_stones[n] += 1

        result = 0

        for n in jewels:
            if n in d_stones:
                result += d_stones[n]

        return result
    
r = Solution()
assert r.numJewelsInStones("aA","aAAbbbb") == 3
assert r.numJewelsInStones("zz","ZZ") == 0
assert r.numJewelsInStones("a","aab") == 2

print("Tests have passed.")