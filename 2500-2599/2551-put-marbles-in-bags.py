# https://leetcode.com/problems/put-marbles-in-bags/

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        adj_sums = []
        for i in range(len(weights)-1):
            adj_sums.append(weights[i] + weights[i+1])
        adj_sums.sort()
        print(adj_sums)
        
        n = len(adj_sums)
        # min_score = sum of k-1 smallest adjacent sums
        min_score = 0
        for i in range(k-1):
            min_score += adj_sums[i]
        # min_score = sum(adj_sums[:k-1])

        # max_score = sum of k-1 largest adjacent sums
        max_score = 0
        for i in range(n-1, n-1-(k-1), -1):
            max_score += adj_sums[i]
        # max_score = sum(adj_sums[-(k-1):])

        return max_score-min_score
