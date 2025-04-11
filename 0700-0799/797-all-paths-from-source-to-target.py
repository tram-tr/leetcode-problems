# https://leetcode.com/problems/all-paths-from-source-to-target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = deque([[0]])
        res = []

        while q:
            path = q.popleft()
            u = path[-1]
            if u == n - 1:
                res.append(path)
                continue
            for v in graph[u]:
                q.append(path + [v])
        
        return res
