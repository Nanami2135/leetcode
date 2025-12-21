class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        left = 0
        right = 0
        up = 0
        down = 0

        for move in moves:
            if move == "L":
                left += 1
            if move == "R":
                right += 1
            if move == "U":
                up += 1
            if move == "D":
                down +=1
        
        if left == right and up == down:
            return True
        
        return False
    
r = Solution()
assert r.judgeCircle("UD") == True
assert r.judgeCircle("LL") == False
assert r.judgeCircle("RUDL") == True

print("Tests have passed.")