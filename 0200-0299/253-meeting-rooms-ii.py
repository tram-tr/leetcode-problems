# https://leetcode.com/problems/meeting-rooms-ii

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        cur = []
        rooms = 0
        for start, end in intervals:
            if not cur or cur[0] > start:
                rooms += 1
            else:
                heappop(cur)
            heappush(cur, end)

        return rooms
