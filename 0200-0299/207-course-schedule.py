# https://leetcode.com/problems/course-schedule/

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        visited = []
        frontier = []
        adj = {}
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            if course not in adj:
                adj[course] = []
            adj[course].append(pre)

        print(adj)

        for course in range(numCourses):
            if course in adj:
                for pre in adj[course]:
                    in_degree[pre] += 1
        
        for course in range(numCourses):
            if (in_degree[course] == 0):
                frontier.append(course)

        while len(frontier) > 0:
            curr = frontier.pop(0)
            visited.append(curr)
            if curr in adj:
                for pre in adj[curr]:
                    in_degree[pre] -= 1
                    if in_degree[pre] == 0:
                        frontier.append(pre)

        return len(visited) == numCourses
        