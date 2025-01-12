# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        left = 0
        s = 0

        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                length = min(length, right - left + 1)
                s -= nums[left]
                left += 1
            
        return length if length != float('inf') else 0
