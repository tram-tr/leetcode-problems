# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [0] * len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(0, len(nums)):
                if visited[i] == 1:
                    continue

                if i > 0 and nums[i - 1] == nums[i] and visited[i - 1] == 0:
                    continue

                path.append(nums[i])
                visited[i] = 1
                dfs(path)
                path.pop()
                visited[i] = 0
            
        dfs([])

        return res
