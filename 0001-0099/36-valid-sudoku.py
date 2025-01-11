# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unique = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row = board[i][j] + f'r{i}'
                    col = board[i][j] + f'c{j}'
                    blk = board[i][j] + f'b{i//3},{j//3}'
                    if row in unique or col in unique or blk in unique:
                        return False
                    unique.add(row)
                    unique.add(col)
                    unique.add(blk)
        
        #print(unqiue)

        return True
