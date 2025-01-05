# https://leetcode.com/problems/contiguous-array/description/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = {0: -1}
        n = len(nums)
        s = 0
        res = 0

        for i in range(n):
            s += nums[i] if nums[i] == 1 else -1
            if s in prefix_sum:
                j = prefix_sum[s] + 1
                res = max(res, i - j + 1)
            else:
                prefix_sum[s] = i
        
        return res
