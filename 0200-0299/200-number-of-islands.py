# https://leetcode.com/problems/number-of-islands

class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     n = len(grid)
    #     m = len(grid[0])
    #     d = [(0,1), (1,0), (0,-1), (-1,0)]
    #     res = 0

    #     def bfs(r, c):
    #         q = deque()
    #         q.append((r, c))

    #         while q:
    #             x, y = q.popleft()
    #             if grid[x][y] == '*':
    #                 continue
    #             grid[x][y] = '*' # mark visited
    #             for dx, dy in d:
    #                 nx = x + dx
    #                 ny = y + dy
    #                 if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
    #                     q.append((nx, ny))

    #     for i in range(n):
    #         for j in range(m):
    #             if grid[i][j] == '1':
    #                 bfs(i, j)
    #                 res += 1

    #     return res

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     n = len(grid)
    #     m = len(grid[0])
    #     res = 0
        
    #     def dfs(r, c):
    #         if r < 0 or r >= n or c < 0 or c >= m:
    #             return
    #         if grid[r][c] == '0':
    #             return

    #         grid[r][c] = '*'
        
    #         dfs(r + 1, c)
    #         dfs(r - 1, c)
    #         dfs(r, c + 1)
    #         dfs(r, c - 1)

    #     for i in range(n):
    #         for j in range(m):
    #             if grid[i][j] == '1':
    #                 dfs(i, j)
    #                 res += 1

    #     return res

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        p = list(range(m * n))

        def check(r, c):
            return 0 <= r < m and 0 <= c < n and grid[r][c] == '1'

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    for dx, dy in d:
                        ni = i + dx
                        nj = j + dy
                        if check(ni, nj):
                            root1 = find(i * n + j)
                            root2 = find(ni * n + nj)
                            if root1 != root2:
                                p[root1] = root2
                                res -= 1

        return res


   
