# https://leetcode.com/problems/count-largest-group/submissions/1482987404/

class Solution:
    def countLargestGroup(self, n: int) -> int:
        hmap = {}
        max_size = 0
        for num in range(1, n + 1):
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10
                num //= 10
            hmap[sum_digits] = hmap.get(sum_digits, 0) + 1
            if hmap[sum_digits] > max_size:
                max_size = hmap[sum_digits]

        count = 0
        for s in hmap.values():
            if s == max_size:
                count += 1

        return count
