# https://leetcode.com/problems/sum-of-two-integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        int_max = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative in 32-bit, convert to signed int
        return a if a <= int_max else ~(a ^ mask)
