# https://leetcode.com/problems/split-array-largest-sum/description/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def condition(x):
            s = 0
            count = 1
            for num in nums:
                s += num
                if s > x:
                    count += 1
                    s = num
            return count <= k

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
