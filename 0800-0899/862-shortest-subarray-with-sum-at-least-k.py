# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        s = 0
        res = len(nums) + 1
        left_prefix = deque() # [left, s]

        for right in range(len(nums)):
            s += nums[right]
            if s >= k: # 0..right
                res = min(res, right + 1)

            # shrinking window
            while left_prefix and left_prefix[-1][1] > s:
                left_prefix.pop()

            while left_prefix and s - left_prefix[0][1] >= k: # left..right
                left = left_prefix[0][0] + 1
                res = min(res, right - left + 1)
                left_prefix.popleft()

            left_prefix.append([right, s])
            
        return res if res <= len(nums) else -1
            
