class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = ""
        
        if len(word1) < len(word2):
            smaller = word1
            bigger = word2
        else:
            smaller = word2
            bigger = word1
        
        for i in range(len(smaller)):
            result += word1[i] + word2[i]
        
        result+= bigger[len(smaller):]
            
        return result

        # for i in range(len(word2) + 1):
        #     if i == len(word1):
        #         result += word2[i:]
        #         break
        #     elif i == len(word2):
        #         result += word1[i:]
        #         break
        #     else:
        #         result += word1[i] + word2[i]

        # return result

r = Solution()
# assert r.mergeAlternately("ab", "cd") == "acbd"
assert r.mergeAlternately("a", "bcd") == "abcd"
assert r.mergeAlternately("abcdffff", "xy") == "axbycdffff"

print("Tests have passed.")
