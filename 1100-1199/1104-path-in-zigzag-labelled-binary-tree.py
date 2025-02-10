# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/description/

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        x = 1
        n = 1
        while (x << 1) <= label:
            x <<= 1
            n += 1

        res = [0] * n
        while n:
            res[n - 1] = label
            label = ((1 << (n - 1)) + (1 << n) - 1 - label) >> 1
            n -= 1

        return res
