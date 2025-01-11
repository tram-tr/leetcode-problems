# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        prefix_sum = {}
        s = 0
        length = -1
        k = sum(nums) - x

        if k == 0:
            return len(nums)

        for i in range(len(nums)):
            s += nums[i]

            if s == k: # 0..i
                length = max(length, i + 1)

            if s - k in prefix_sum: # j..i
                j = prefix_sum[s - k] + 1
                length = max(length, i - j + 1)
            
            if s not in prefix_sum:
                prefix_sum[s] = i

        if length != -1:
            return len(nums) - length
        else:
            return -1
