# https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/description/

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        def dfs(v, target_w, adj, visited):
            visited[v] = 1
            res = 1
            for u, w in adj[v]:
                if w <= target_w and not visited[u]:
                    res += dfs(u, target_w, adj, visited)
            return res

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[v].append((u, w))

        left = 1
        right = 1000001
        while left < right:
            mid = (left + right) // 2
            visited = [0] * n
            if dfs(0, mid, adj, visited) == n:
                right = mid
            else:
                left = mid + 1

        return left if left != 1000001 else -1
