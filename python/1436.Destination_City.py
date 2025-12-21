from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        start = {}
        end = {}
        for n in paths:
            if n[0] not in start:
                start[n[0]] = 1
            else:
                start[n[0]] += 1
            if n[1] not in end:
                end[n[1]] = 1
            else:
                end[n[1]] = 1
            
        for n in start:
            if n in end:
                end[n] -= 1
                if end[n] == 0:
                    end.pop(n)

        for n in end:
            return n
    
            




        print (start)
        print (end)



r = Solution()
# assert r.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]) == "Sao Paulo"
assert r.destCity([["B","C"],["D","B"],["C","A"]]) == "A"
assert r.destCity([["A","Z"]]) == "Z"
print("Tests have passed.") 