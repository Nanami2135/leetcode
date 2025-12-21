class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        s_count = {}
        t_count = {}

        for letter in s:
            if letter in s_count:
                s_count[letter] += 1
            else:
                s_count[letter] = 1

        for letter in t:
            if letter in t_count:
                t_count[letter] += 1
            else:
                t_count[letter] = 1

        for key in t_count.keys():
            
            if t_count[key] != s_count.get(key, -1):
                
                return key
    
        return ""
 
r = Solution()
assert r.findTheDifference("", "a") == "a"
assert r.findTheDifference("aasd", "aaasd") == "a"

print("Tests have passed.")

