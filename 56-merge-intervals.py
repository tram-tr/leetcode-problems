# https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
    
        intervals.sort(key = lambda x: x[0]) # sort by start time
        merged = []
        for start, end in intervals:
            if (len(merged) > 0 and merged[-1][1] >= start):
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        return merged