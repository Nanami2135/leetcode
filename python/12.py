class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        
        return len(l[len(l)-1])



r = Solution()
assert r.lengthOfLastWord("Hello World") == 5
assert r.lengthOfLastWord("   fly me   to   the moon  ") == 4

print("Tests have passed.")        