# https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(x, y, index):
            if index == len(word):
                return True
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                return False
            if board[x][y] != word[index]:
                return False

            curr = board[x][y]
            board[x][y] = ''

            for dx, dy in d:
                if dfs(x + dx, y + dy, index + 1):
                    return True

            board[x][y] = curr
    
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
