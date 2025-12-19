class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split(" ")
        result = ""
        for word in string:
            for i in range(len(word)-1,-1,-1):
                result += word[i]
                if i == 0:
                    result += " "
        
        return result[:len(result)-1]


        # i = 0
        # j = 0
        # while i <= len(s) - 1:
        #     j = s[j + 1:].find(" ")
        #     for n in range(i,j):
        #         s[i],s[j] = s[j],s[i]
        #         i += 1
        #         j -= 1
        #         if i >= j:
        #             break
        #     i = j


r = Solution()
assert r.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert r.reverseWords(["H","a","n","a","a","h"]) == ["h","a","a","n","a","H"]
assert r.reverseWords(["a","b","c","d","e"]) == ["e","d","c","b","a"]
print("Tests have passed.") 


        