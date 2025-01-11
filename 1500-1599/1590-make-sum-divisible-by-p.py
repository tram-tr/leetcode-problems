# https://leetcode.com/problems/make-sum-divisible-by-p/description/

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        prefix_sum = {}
        s = 0
        length = len(nums)
        sum_n = sum(nums)
        k = sum_n % p

        if k == 0:
            return 0

        for i in range(len(nums)):
            s += nums[i]

            if (sum_n - s) % p == 0: # 0..i
                length = min(length, i + 1)
            
            mod = (s % p - k) % p
            if mod in prefix_sum: # j..i
                j = prefix_sum[mod] + 1
                length = min(length, i - j + 1)
            
            prefix_sum[s % p] = i
    
        if length < len(nums):
            return length
        else:
            return -1
        
