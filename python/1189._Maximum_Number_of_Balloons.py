from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        word = "balloon"
        d_text = defaultdict(int)
        d_word = defaultdict(int)

        for n in text:
            d_text[n] += 1
        for n in word:
            d_word[n] += 1

        result = 10000000000

        for key in d_word:
            if d_text[key] == 0:
                return 0
            # if d_text[key] >= d_word[key]:
            #     r = int(d_text[key] // d_word[key])
            # if d_text[key] < d_word[key]:
            #     return 0 
            r = int(d_text[key] // d_word[key])
            if r == 0:
                return 0
            result = min(result,r)

        return result
        

# b:1
# a:1
# l:2
# o:2
# n:1

# n:1
# l:2
# a:1
# b:1
# o:2
# k:1

r = Solution()
assert r.maxNumberOfBalloons("nlaebolko") == 1
assert r.maxNumberOfBalloons("loonbalxballpoon") == 2
assert r.maxNumberOfBalloons("leetcode") == 0
print("Tests have passed.") 