from typing import List

from typing import List


def get_min_potion(spell, success) -> int:
    if success % spell != 0:
        return success // spell + 1
    return success / spell


def binary_search(arr: list, l: int, r: int, x: int) -> int:
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = {}
        potions.sort()
        successes = [0] * len(spells)
        for i, spell in enumerate(spells):
            min_potion = get_min_potion(spell, success)
            if min_potion not in m:
                min_potion_id = binary_search(potions, 0, len(potions), min_potion)
                num_potions = len(potions) - min_potion_id
            else:
                num_potions = m[min_potion]
            successes[i] = num_potions

            m[min_potion] = num_potions

        return successes

r = Solution()
assert r.successfulPairs([5,1,3],[1,2,3,4,5],7) == [4,0,3]
assert r.successfulPairs([3,1,2],[8,5,8],16) ==  [2,0,2]

# assert binary_search([1, 2, 3, 4, 5], 0, 4, 2) == 1
# arr = [2, 2, 2]
# x = 0
# assert binary_search(arr, 0, len(arr) - 1, x) == -1
arr = [0, 1, 1, 1, 1, 2, 2, 2]
x = 1
assert binary_search(arr, 0, len(arr) - 1, x) == 1
arr = [0, 0, 2, 2, 3]
x = 1
result = binary_search(arr, 0, len(arr) - 1, x)
assert result == 2, f"Result was {result}"

print("Tests have passed.")