# https://leetcode.com/problems/subarray-product-less-than-k/description/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        count = 0
        
        if k <= 1:
            return 0

        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1
        return count
