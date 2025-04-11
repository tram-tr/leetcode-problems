# https://leetcode.com/problems/meeting-rooms-ii

# from heapq import heappush, heappop

# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         intervals.sort()

#         cur = []
#         rooms = 0
#         for start, end in intervals:
#             if not cur or cur[0] > start:
#                 rooms += 1
#             else:
#                 heappop(cur)
#             heappush(cur, end)

#         return rooms

class Solution(object):
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    meetings = []
    for i in intervals:
      meetings.append((i.start, 1))
      meetings.append((i.end, 0))
    meetings.sort()
    ans = 0
    count = 0
    for meeting in meetings:
      if meeting[1] == 1:
        count += 1
      else:
        count -= 1
      ans = max(ans, count)
    return ans

