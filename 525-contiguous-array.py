# https://leetcode.com/problems/contiguous-array/description/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = {}
        n = len(nums)
        s = 0
        res = 0

        for i in range(n):
            s += nums[i] if nums[i] == 1 else -1
            if s == 0:
                res = max(res, i + 1)
            if s in prefix_sum:
                j = prefix_sum[s] + 1
                res = max(res, i - j + 1)
            else:
                prefix_sum[s] = i
        
        return res
