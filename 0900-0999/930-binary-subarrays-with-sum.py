# https://leetcode.com/problems/binary-subarrays-with-sum/description/

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix_sum = {}
        s = 0
        count = 0

        for i in range(len(nums)):
            s += nums[i]

            if s == goal:
                count += 1
            
            if s - goal in prefix_sum:
                count += prefix_sum[s - goal]
            
            prefix_sum[s] = prefix_sum.get(s, 0) + 1

        return count 
