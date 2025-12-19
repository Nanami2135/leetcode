from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # if len(s) <= 1:
        #     return s
        i = 0
        j = len(s) - 1
            
        while True:
            s[i],s[j] = s[j],s[i]

            if i == j or j - i == 1:
                break

            i += 1
            j -= 1
        
        return s
    
# Hannah
# 012345
# __ij__
r = Solution()
assert r.reverseString(["a"]) == ["a"]
assert r.reverseString(["H","a","n","a","a","h"]) == ["h","a","a","n","a","H"]
assert r.reverseString(["a","b","c","d","e"]) == ["e","d","c","b","a"]
print("Tests have passed.")  