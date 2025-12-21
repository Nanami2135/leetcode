class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        
        player_a = []
        plaayer_b = []
        for i in range(len(moves)):
            if i % 2 == 0:
                player_a.append(moves[i])
            else:
                plaayer_b.append(moves[i])

        wins_combinetions = [[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]
        game_steps = {}
        n = 0
        for step in player_a:
            for i in wins_combinetions[n]:
                if step == i:
                    if step in game_steps:
                        game_steps[step] +=1 
                    else:
                        game_steps[step] = 1
            n+=1


r = Solution()
assert r.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]) == "A"
assert r.tictactoe("LL") == False
assert r.tictactoe("RUDL") == True

print("Tests have passed.")