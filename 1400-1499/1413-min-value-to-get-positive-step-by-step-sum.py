# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        min_start = 1
        
        for i in range(len(nums)):
            s += nums[i]
            min_start = max(min_start, 1 - s)

        return min_start

        
