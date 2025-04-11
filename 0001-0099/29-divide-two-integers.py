# https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend = -dividend if dividend > 0 else dividend
        divisor = -divisor if divisor > 0 else divisor
        res = 0

        while dividend <= divisor:
            x = divisor
            count = 1
            while x >= (-(2**30)) and dividend <= (x << 1):
                x <<= 1
                count <<= 1
            dividend -= x
            res += count
        return res if sign else -res
