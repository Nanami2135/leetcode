class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = []

        for i in range (len(operations)):
            try:
                result.append(int(operations[i])) 
            except:
                if operations[i] == "+":
                    result.append(result[len(result)-1] + result[len(result)-2])
                if operations[i] == "D":
                    result.append(result[len(result)-1] * 2)
                if operations[i] == "C":
                    result = result[:len(result)-1]
        
        return_res = 0
        for number in result:
            return_res += number
        
        return return_res




r = Solution()
assert r.calPoints(["5","2","C","D","+"]) == 30
# assert r.calPoints("   fly me   to   the moon  ") == 4

print("Tests have passed.")  