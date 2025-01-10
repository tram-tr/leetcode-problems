# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, h: List[int]) -> int:
        left = 0
        right = len(h) - 1
        res = 0
        while left < right:
            area = (right - left) * min(h[left], h[right])
            res = max(res, area)
            if h[left] > h[right]:
                right -= 1
            else:
                left += 1


        return res
