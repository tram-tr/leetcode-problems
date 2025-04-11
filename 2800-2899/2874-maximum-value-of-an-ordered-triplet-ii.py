# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = m = m_diff = 0
        for num in nums:
            res = max(res, m_diff * num)
            m = max(m, num)
            m_diff = max(m_diff, m - num)

        return res
