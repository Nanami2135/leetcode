class Solution(object):
    def summSymbols(self, a, b):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        zero_add_zero = 0 
        one_add_zero = 1
        one_add_one = 2

        first = []
        second = []

        for symbol in a:
            first.append(int(symbol))
        for symbol in b:
            second.append(int(symbol))

        if len(first)>=len(second):
            size = len(first) + 1
            second = [0]*(len(first) - len(second)) + second
        else:
            size = len(second) + 1
            first = [0]*(len(second) - len(first)) + first

        result = [0] * size

        for i in range(size-2,-1,-1):
            if first[i] + second[i] == 2:
                result[i+1] += 0
                result[i] += 1
                if result[i] == 2:
                    result[i] = 1
                    result[i-1] = 1
            if first[i] + second[i] == 1:
                result[i+1] += 1
                if result[i+1] == 2:
                    result[i+1] = 0
                    result[i] = 1
            if first[i]+ second[i] == 0:
                result[i+1]+=0
        
        result_string = "" 
        for symbol in result:
            result_string += str(symbol)
        
        if result_string[0] == "0":
            return result_string[1:]

        return result_string
         
r = Solution()
assert r.summSymbols("1111", "1111") == "11110"
assert r.summSymbols("101", "1") == "110"

print("Tests have passed.")

