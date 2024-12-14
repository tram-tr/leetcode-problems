# https://leetcode.com/problems/subarray-sum-equals-k/description/

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        curr_sum = 0
        sum_freq = {0: 1}

        for num in nums:
            curr_sum += num
            if (curr_sum - k) in sum_freq:
                count += sum_freq[curr_sum - k]
            sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1

        return count