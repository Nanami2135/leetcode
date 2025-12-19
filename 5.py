class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        factors = set()
        for i in range(1, int(len(s)**0.5) + 1):
            if len(s) % i == 0:
                factors.add(i)
                factors.add(len(s) // i)
        
        factors = sorted(factors, reverse=True)[1:]

        for f in factors:
            # print(f"factor: {f}")
            num_substrings = len(s) // f
            first_substring = s[:f]
            # print(f"first substring: {first_substring}")

            comparison_succeeded = True
            for i in range(1, num_substrings):
                curr_substring = s[i * f: (i + 1) * f]
                if curr_substring != first_substring:
                    comparison_succeeded = False
                    break

            if comparison_succeeded:
                return True
                
        return False

        # splitted_string = ""
        # result = None
        # for number in range(len(factors) - 1):
        #     splitted_string = [s[i:i+factors[number]] for i in range(0, len(s), factors[number])]



        #     for j in range(len(splitted_string) - 1):
        #         if splitted_string[j] != splitted_string[j + 1]:
        #             result = False 
        #         else:
        #             result =  True
        #             if splitted_string[j] == len(splitted_string) -1 and result == True:
        #                 return True
                        
                
        # return False
                    
        
        
                    



r = Solution()
# assert r.repeatedSubstringPattern("abcabc") == True
# assert r.repeatedSubstringPattern("abaabaabaaba") == True
assert r.repeatedSubstringPattern("abcdabcc") == False

print("Tests have passed.")