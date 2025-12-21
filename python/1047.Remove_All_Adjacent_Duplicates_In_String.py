class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for n in s:
            if stack == []:
                stack.append(n)
            else:
                if stack[-1] == n:
                    stack.pop()
                else:
                    stack.append(n) 
        
        result = ""
        for m in stack:
            result += m

        return result
        

        
        

r = Solution()
assert r.removeDuplicates(s = "azxxzy") == "ay"
# assert r.removeDuplicates("()[]{}") == True
# assert r.removeDuplicates("()[]{}") == True
# assert r.removeDuplicates("()[]{}") == True

print("Tests have passed.")