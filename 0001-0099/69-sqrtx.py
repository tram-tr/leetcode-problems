# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 >= x:
                right = mid
            else:
                left = mid + 1

        return left if left ** 2 <= x else left - 1
