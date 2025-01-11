# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = Counter()
        max_length = 0
        j = 0
        for i in range(len(nums)):
            counter[nums[i]] += 1
            if counter[nums[i]] > k:
                while nums[i] != nums[j]:
                    counter[nums[j]] -= 1
                    j += 1
                counter[nums[j]] -= 1
                j += 1
            max_length = max(max_length, i - j + 1)
        return max_length
