class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)
       
        
        no_repeat = {}
        window_len = 0
        i = j = 0

        while j < len(s):
            if s[j] not in no_repeat:
                no_repeat[s[j]] = j
                j += 1
                
            else:
                window_len = max(window_len, j - i)
                no_repeat.pop(s[i])
                i += 1
                
        return max(window_len,len(no_repeat))

        # no_rapiting = set()
        # result = 0
        # i = j = 0


        # while i < len(s):
        #     if s[i] in no_rapiting:
        #         result = max(result,len(no_rapiting))
        #         no_rapiting.clear()
        #         j += 1
        #         no_rapiting.add(s[j])
        #         i = j
 
        #     no_rapiting.add(s[i])
        #     i +=1   

        # return max(result,len(no_rapiting))
        
r = Solution()
assert r.lengthOfLongestSubstring("anviaj") == 5
assert r.lengthOfLongestSubstring("dvdf") == 3
assert r.lengthOfLongestSubstring("pwwkew") == 3

print("Tests have passed.")

                 
 
