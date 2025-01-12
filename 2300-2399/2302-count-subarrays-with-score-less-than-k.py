# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        s = 0
        count = 0

        for right in range(len(nums)):
            s += nums[right]
            while (right - left + 1) * s >= k:
                s -= nums[left]
                left += 1

            count += right - left + 1 
        
        return count
