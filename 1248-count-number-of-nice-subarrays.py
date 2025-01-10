# https://leetcode.com/problems/count-number-of-nice-subarrays/description/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(h):
            left = 0
            count = 0
            if h < 0:
                return 0
            s = 0
            for right in range(len(nums)):
                s += nums[right] % 2
                while s > h:
                    s -= nums[left] % 2
                    left += 1
                count += right - left + 1
            return count
        
        return atMost(k) - atMost(k-1)
