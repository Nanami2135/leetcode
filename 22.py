from typing import List
class Solution:
    def average(self, salary: List[int]) -> float:

        min_sal = salary[0]
        max_sal = 0
        all_salary = 0

        for price in salary:
            if price < min_sal:
                min_sal = price
            if price > max_sal:
                max_sal = price
            all_salary += price
        
        return float((all_salary - min_sal - max_sal)/(len(salary) - 2))
            

        

r = Solution()
assert r.average([4000,3000,1000,2000]) == 2500.00000
assert r.average([1000,2000,3000]) == 2000.00000
print("Tests have passed.")  