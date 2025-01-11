# https://leetcode.com/problems/rotting-oranges/description/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if n == 0:
            return -1
        
        fresh_count = 0
        rotten = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        time = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while rotten and fresh_count > 0:
            time += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in directions:
                    xx = x + dx
                    yy = y + dy
                    if xx < 0 or xx == n or yy < 0 or yy == m:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    fresh_count -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))

        # for row in grid:
        #     print(row)

        return time if fresh_count == 0 else -1
