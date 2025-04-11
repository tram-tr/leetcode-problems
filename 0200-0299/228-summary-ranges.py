# https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def f(i, j):
            if i == j:
                return str(nums[i])
            else:
                return f'{nums[i]}->{nums[j]}'

        i = 0
        n = len(nums)
        res = []

        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1
            res.append(f(i, j))
            i = j + 1

        return res
