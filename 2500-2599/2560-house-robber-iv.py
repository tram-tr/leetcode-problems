# https://leetcode.com/problems/house-robber-iv

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def cond(x):
            count = 0
            j = -2
            for i in range(len(nums)):
                if nums[i] > x or i == j + 1:
                    continue
                count += 1
                j = i

            return count >= k
            
        left = 0
        right = max(nums)

        while left < right:
            mid = left + (right - left) // 2
            if cond(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
