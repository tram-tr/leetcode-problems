# https://leetcode.com/problems/design-a-leaderboard

'''
map = { 1 : 30 }
list.add ( (30, 1) )

(30, 1)
(39, 1)
'''
from sortedcontainers import SortedList
class Leaderboard:
    def __init__(self):
        self.map = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.map:
            self.map[playerId] = 0
        self.map[playerId] += score

    def top(self, K: int) -> int:
        return sum(x for x in sorted(self.map.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        del self.map[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
