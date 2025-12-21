class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for n in s:
            if n == "[" or n == "{" or n == "(":
                stack.append(n)
            if n == "]" or n == "}" or n == ")":
                m = stack[-1]
                if m + n == "[]" or m + n == "{}" or m + n == "()":
                    stack.pop()
                else:
                    return False
        
        return True



r = Solution()
assert r.isValid("()") == True
assert r.isValid("()[]{}") == True
assert r.isValid("(]") == False
assert r.isValid("([])") == True

print("Tests have passed.")
        