# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(list(curr))
                return
    
            curSet = set(curr)
            for i in range(len(nums)):
                if nums[i] not in curSet:
                    curr.append(nums[i])
                    dfs(curr)
                    curr.pop()

        dfs([])

        return res
