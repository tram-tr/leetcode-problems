# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, curr):
            res.append(list(curr))

            for i in range(index, len(nums)):
                if  i > index and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])
        return res
