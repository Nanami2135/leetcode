from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        """
        Do not return anything, modify board in-place instead.
        """
        bord_column_first = board[0]
        bord_column_second = board[len(board)-1]
        board_row_first = []
        board_row_second = []

        for n in board:
            board_row_first.append(n[0])
            board_row_second.append(n[len(n)-1])

        zero_board_position = () 

        for i in range(len(bord_column_first)):
            if bord_column_first[i] == "O":
                zero_board_position += (0,i)
        for i in range(len(bord_column_second)):
            if bord_column_second[i] == "O":
                zero_board_position += (len(board)-1,i)
        for i in range(len(board_row_first)):
            if board_row_first[i] == "O":
                zero_board_position += (i,0)
        for i in range(len(board_row_second)):
            if board_row_second[i] == "O":
                zero_board_position += (i,len(board_row_second)-1)

        row = 0
        col = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and i == 0:
                    zero_board_position += (i,j)
                if board[i][j] == "0" and (i-1,j) not in zero_board_position:
                    board[i][j] = "X"
        
        print (board)

                


            

        














        i = 0
        j = 0
        zero_position = None

        while i != len(board):
            for index in range(len(board[i])):
                if board[i][index] == "O" and i == 0:
                    zero_position = index
                    j = i
                    
                    continue
                if board[i][index] == "O" and index == j:
                    i += 1
                else:
                    board[i][index] = "X"
            i += 1






        

r = Solution()
assert r.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]) == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
assert r.solve([["X"]]) == [["X"]]


print("Tests have passed.")