# https://leetcode.com/problems/find-the-longest-equal-subarray/description/

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        left = 0
        window = defaultdict(int)
        max_freq = 0

        for right in range(len(nums)):
            window[nums[right]] += 1
            max_freq = max(max_freq, window[nums[right]])
            # max_freq = max(window.values())
            
            while right - left + 1 - max_freq > k:
                window[nums[left]] -= 1
                left += 1

        return max_freq
