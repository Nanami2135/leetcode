class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x = sorted(s)
        y = sorted(t)
        if x == y:
            return True
        else:
            return False
        

r = Solution()
assert r.isAnagram("anagram", "nagaram") == True
assert r.isAnagram("rat", "car") == False

print("Tests have passed.")