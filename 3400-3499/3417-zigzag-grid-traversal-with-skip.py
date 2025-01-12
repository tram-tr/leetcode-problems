# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/description/

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        res = []
        
        for i in range(n):
            if i % 2 == 0:
                for j in range(0, m, 2):
                    res.append(grid[i][j])
            else:
                for j in range(m - 1 - m % 2, -1, -2):
                    res.append(grid[i][j])
                    
        return res
            
            
