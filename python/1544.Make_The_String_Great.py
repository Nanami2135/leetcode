class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        stack = [s[0]]
        for i in range(1,len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            # elif s[i].isupper():
            #     if stack[-1] == s[i].lower():
            #         stack.pop()
            #     else: 
            #         stack.append(s[i])
            # elif s[i].islower:
            #     if stack[-1] == s[i].upper():
            #         stack.pop()
            #     else: 
            #         stack.append(s[i])
            elif stack[-1] != s[i] and stack[-1].upper() == s[i].upper():
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)



        

r = Solution()
assert r.makeGood("leEeetcode") == "leetcode"
assert r.makeGood("abBAcC") == ""
assert r.makeGood("s") == "s"

print("Tests have passed.")