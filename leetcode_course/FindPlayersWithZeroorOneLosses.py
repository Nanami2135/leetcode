from typing import List, Dict


NO_MATCHES = 0
ONE_WIN = 1
ONE_LOSS = 2
MULTIPLE_LOSSES = 3


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        r: Dict[int, int] = {}
        # States:
        # 0 -- default, no games played
        # 1 -- one win
        # 2 -- one loss
        # 3 -- multiple losses
        for match in matches:
            winner = match[0]
            loser = match[1]

            # Win
            s1 = r.get(winner, NO_MATCHES)
            if s1 == NO_MATCHES: #or s1 == 1:
                r[winner] = ONE_WIN
            
            # Loss
            s2 = r.get(loser, NO_MATCHES)
            if s2 == NO_MATCHES or s2 == ONE_WIN:
                r[loser] = ONE_LOSS
            elif s2 == ONE_LOSS:
                r[loser] = MULTIPLE_LOSSES
        

        one_win = []
        one_loss = []
        for player in r:
            if r[player] == ONE_WIN:
                one_win.append(player)
            elif r[player] == ONE_LOSS:
                one_loss.append(player)

        one_win.sort()
        one_loss.sort()

        return [one_win, one_loss]




        
        

        # win = set()
        # loss = set()
        # one_loss = set()

        # for play in matches:
        #     win.add(play[0])
        #     if play[1] in  loss and play[1] not in one_loss:
        #         one_loss.remove(play[1])
        #         continue
        #     loss.add(play[1])
        #     if play[1] not in one_loss:    
        #         one_loss.add(play[1])
        #     else:
        #         one_loss.remove(play[1])
        
        # remove_players = []

        # for player in win:
        #     if player in loss:
        #         remove_players.append(player)
        
        # for players in remove_players:
        #     win.remove(players)
            
        # result = [list(win),list(one_loss)]
        
        # return result
            
        
r = Solution()
assert r.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]) == [[1,2,10],[4,5,7,8]]
assert r.findWinners([[2,3],[1,3],[5,4],[6,4]]) == [[1,2,5,6],[]]
assert r.findWinners([[1,5],[2,5],[2,8],[2,9],[3,8],[4,7],[4,9],[5,7],[6,8]]) == [[1,2,3,4,6],[]]
print("Tests have passed.") 
