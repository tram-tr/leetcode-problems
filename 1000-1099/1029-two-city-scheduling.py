# https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        base = sum(c[0] for c in costs)
        delta = sorted(c[1] - c[0] for c in costs)
        return base + sum(delta[:len(costs) // 2])
