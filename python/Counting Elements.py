from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:

        our_arr = set(arr)
        result = 0

        for n in arr:
            need = n + 1
            if need in our_arr:
                result += 1

        return result 





r = Solution()
assert r.countElements([1,2,3]) == 2
assert r.countElements([1,1,3,3,5,5,7,7]) == 0

print("Tests have passed.")