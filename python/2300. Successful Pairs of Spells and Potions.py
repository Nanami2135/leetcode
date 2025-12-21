from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        d = {}


        potions.sort()

        totol_successes_by_spell = []
        # str_succes = len(str(abs(success)))

        
        while True:

            # for oneSpell in spells:
            #     if oneSpell*potions[0]>= success:
            #         totol_successes_by_spell.append(len(potions))
            #         continue

            for oneSpell in spells:
                
                if oneSpell*potions[0]>= success:
                    totol_successes_by_spell.append(len(potions))
                    continue
                if oneSpell*potions[-1] < success:
                    totol_successes_by_spell.append(0)
                    continue

                if oneSpell in d:
                    totol_successes_by_spell.append(d[oneSpell])
                    continue

                start = 0
                end = len(potions) -1
                successes_by_spell = 0

                while True:

                    if start > end:
                       totol_successes_by_spell.append(successes_by_spell)
                       d[oneSpell] = successes_by_spell
                       break
                    if start == end:
                        middle = start 
                    else:
                        middle = (start + end) // 2 
                        
                    if oneSpell * potions[middle] >= success:
                        successes_by_spell += len(potions[middle:end]) + 1
                        if oneSpell * potions[middle - 1] >= success:
                            end = middle - 1
                            continue
                        totol_successes_by_spell.append(successes_by_spell)
                        d[oneSpell] = successes_by_spell
                        break
                    if  oneSpell * potions[middle] <= success:
                        start = middle + 1
                        continue
                    if start > end:
                        totol_successes_by_spell.append(successes_by_spell)
                        d[oneSpell] = successes_by_spell
                        break
    
            break
        
        return totol_successes_by_spell 



r = Solution()
assert r.successfulPairs([15,8,19],[38,36,23],328) == [3,0,3]
assert r.successfulPairs([3,1,2],[8,5,8],16) ==  [2,0,2]


print("Tests have passed.")