# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description/

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])
        dp = [[[float('-inf') for _ in range(3)] for _ in range(m)] for _ in range(n)]

        for count in range(3):
            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    if i == n - 1 and j == m - 1:
                        dp[i][j][count] = max(0, coins[i][j]) if count > 0 else coins[i][j]
                        continue

                    ans = float('-inf')
                    if i + 1 < n:
                        ans = max(ans, coins[i][j] + dp[i + 1][j][count])
                        if count > 0: 
                            ans = max(ans, dp[i + 1][j][count - 1])
                    if j + 1 < m:
                        ans = max(ans, coins[i][j] + dp[i][j + 1][count])
                        if count > 0: 
                            ans = max(ans, dp[i][j + 1][count - 1])
                    dp[i][j][count] = ans

        return dp[0][0][2]
