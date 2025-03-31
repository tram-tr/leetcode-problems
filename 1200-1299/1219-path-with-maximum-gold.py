# https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (1,0), (0, -1), (-1, 0)]
        def dfs(row, col):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
                return 0

            val = grid[row][col]
            grid[row][col] = 0
            
            curr = 0
            for dr, dc in dir:
                if row + dr < len(grid) and col + dc < len(grid[0]) and grid[row + dr][col + dc] != 0:
                    curr = max(curr, dfs(row + dr, col + dc))
            
            grid[row][col] = val
            return curr + val

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    res = max(res, dfs(row, col))
            
        return res
