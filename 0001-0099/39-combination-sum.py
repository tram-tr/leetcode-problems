# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(index, s, path):
            if s == target:
                res.append(list(path))
                return

            if s > target:
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                s += candidates[i]
                dfs(i, s, path)
                s -= candidates[i]
                path.pop()

        dfs(0, 0, [])
        return res
