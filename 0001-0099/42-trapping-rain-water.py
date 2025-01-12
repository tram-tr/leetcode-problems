# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        left_h = height[left]
        right_h = height[right]

        while left < right:
            if left_h <= right_h:
                res += left_h - height[left]
                left += 1
                left_h = max(left_h, height[left])
            else:
                res += right_h - height[right]
                right -= 1
                right_h = max(right_h, height[right])

        return res
