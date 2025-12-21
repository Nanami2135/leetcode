from typing import Tuple, List


class Solution:
    def partition(self, number:int, massiv:list, sum_pow:int) -> Tuple[List[int], int]:
        
        max_power = 10
        counter = 0
        while True:
            number = number/2
            counter += 2
            if number < max_power:
                if massiv == []:

                    massiv = [abs(int(number))]*counter
                    sum_pow = abs(int(number))*counter
                else:
                    for i in range(counter):
                        massiv.append(abs(int(number)))
            break
        return massiv, sum_pow
            
    def myPow(self, x: float, n: int) -> float:
        needed_number_pow = n
        max_power = 10
        pow_number = [1,x,0,0,0,0,0,0,0,0,0]
        pow_needed_number_partition = []
        counter = 0
        sum_pow = 0
        result = 0
        if abs(n) > 3:
            pow_needed_number_partition, sum_pow = self.partition(n,pow_needed_number_partition,sum_pow)
        else:
            pow_needed_number_partition.append(abs(int(n)))
            sum_pow += int(n)

        while True:    
            if sum_pow != needed_number_pow:
                pow_needed_number_partition, sum_pow = self.partition(self,n,pow_needed_number_partition,sum_pow)
            else:
                break

        required_number = x 
        for i in range(2,pow_needed_number_partition[0] + 1):
            required_number *= x
            pow_number[i] = required_number
        
        for number in pow_needed_number_partition:
            if result == 0:
                result = pow_number[number]
            else:
                result *= pow_number[number]
        if n < 0:
            return round(1/result, 5)
    
        return round(result, 5)

            
r = Solution()
assert r.myPow(2.00000, 10) == 1024.00000
assert r.myPow(1.00012,2048) == 9.26100
assert r.myPow(2.00000, -2) == 0.25
print("Tests have passed.")  