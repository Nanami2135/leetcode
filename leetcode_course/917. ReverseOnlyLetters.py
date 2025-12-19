from collections import deque


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        dq = deque()
        if (len(s) - 1) % 2 == 0:
            i = j = (len(s) - 1) / 2
            dq.append(s[i])
            i -= 1
            j += 1
        else:
            i = (len(s) - 1) // 2
            j = i + 1
        while i >= 0 and j<= len(s) - 1:
            if s[i].isalpha and s[j].isalpha:
                dq.append(s[i])
                dq.appendleft(s[j])
                i -= 1
                j += 1
            elif s[i].isalpha:
                dq.append(s[j])
                j += 1
            elif s[j].isalpha:
                dq.appendleft(s[i])
                i -= 1
            else:
                dq.append(s[j])
                dq.appendleft(s[i])
                i -= 1
                j += 1

                

                


                
            

            

        # a = ""
        # b = ""
        # i = 0
        # j = len(s) - 1
        # while i <= j:
        #     if s[i].isalpha() and s[j].isalpha():
        #         if i == j:
        #             a += s[i]
        #             break
        #         a += s[j]
        #         b += s[i]
        #         i += 1
        #         j -= 1
        #     elif s[i].isalpha():
        #         b += s[j]
        #         j -= 1
        #     elif s[j].isalpha():
        #         a += s[i]
        #         i += 1
        #     else:
        #         if i == j:
        #             a += s[i]
        #             break
        #         else:
        #             a += s[i]
        #             b += s[j]
        #             i += 1
        #             j -= 1

        # res=''.join(reversed(b))
            
        # result = a + res
        # return result


r = Solution()
assert r.reverseOnlyLetters("ab-cd") == "dc-ba"
assert r.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
assert r.reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
print("Tests have passed.") 
