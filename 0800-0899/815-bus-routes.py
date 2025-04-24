# https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        adjList = defaultdict(set)
        stop_to_buses = defaultdict(set)
        for i in range(len(routes)):
            for stop in routes[i]:
                stop_to_buses[stop].add(i)
            for j in range(len(routes)):
                if i == j:
                    continue
                if set(routes[i]).intersection(set(routes[j])):
                    adjList[i].add(j)

       
        start = stop_to_buses[source]
        end = stop_to_buses[target]
        q = deque()
        visited = set()
        for bus in start:
            q.append((bus, 1))
            visited.add(bus)

        while q:
            curr, count = q.popleft()
            if curr in end:
                return count
            
            for nxt in adjList[curr]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, count + 1))

        return -1
