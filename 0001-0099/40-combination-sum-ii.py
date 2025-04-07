# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(index, s, path):
            if s == target:
                res.append(path[:])
                return

            if s > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                s += candidates[i]
                path.append(candidates[i])
                dfs(i + 1, s, path)
                s -= candidates[i]
                path.pop()

        dfs(0, 0, [])
        return res
