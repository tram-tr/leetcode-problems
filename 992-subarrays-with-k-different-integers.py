# https://leetcode.com/problems/subarrays-with-k-different-integers/description/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(h):
            left = 0
            window = defaultdict(int)
            count = 0
            for right in range(len(nums)):
                window[nums[right]] += 1
                while len(window) > h:
                    window[nums[left]] -= 1
                    if window[nums[left]] == 0:
                        del window[nums[left]]
                    left += 1
                count += right - left + 1
            return count


        return at_most(k) - at_most(k - 1)
