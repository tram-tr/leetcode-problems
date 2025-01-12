# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        max_sum = window

        for right in range(k, len(nums)):
            left = right - k
            window += nums[right] - nums[left]
            if window > max_sum:
                max_sum = window
            
        return max_sum / k
