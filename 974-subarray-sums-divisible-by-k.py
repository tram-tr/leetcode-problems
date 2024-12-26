# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = {}
        s = 0
        count = 0

        for i in range(len(nums)):
            s += nums[i]

            if s % k == 0: # 0..i
                count += 1

            if s % k in prefix_sum: # j..i
                count += prefix_sum[s % k]
            
            prefix_sum[s % k] = prefix_sum.get(s % k, 0) + 1

        return count
