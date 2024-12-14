# https://leetcode.com/problems/daily-temperatures/description/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                t, idx = stack.pop()
                answer[idx] = i - idx
                
            stack.append((temperatures[i], i))

        return answer
