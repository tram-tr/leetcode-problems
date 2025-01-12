# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        left = 0
        min_idx = -1
        max_idx = -1

        for right in range(len(nums)):
            # shrinking window
            if nums[right] < minK or nums[right] > maxK:
                min_idx = -1
                max_idx = -1
                left = right + 1

            if nums[right] == minK:
                min_idx = right
            if nums[right] == maxK:
                max_idx = right

            res += max(0, min(min_idx, max_idx) - left + 1)

        return res
