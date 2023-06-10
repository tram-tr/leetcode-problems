class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = [1, 2, 5]
        # amount = 8
        #       0   1   2   3   4   5   6   7   8  
        # dp = [inf,inf,inf,inf,inf,inf,inf,inf,inf]
        # dp = [ 0,  1,  1,  2,  2,  1,  2,  2,  3]
        
        # Time: O(N*M)
        # Space: O(N*M)
        if (amount == 0):
            return 0
        
        dp = [12 * 10000] * (amount + 1)
        dp[0] = 0

        for curr in range(amount + 1):
            for coin in coins:
                if (curr >= coin):
                    dp[curr] = min(dp[curr], dp[curr-coin] + 1)
        
        if (dp[-1] == 12 * 10000):
            return -1
        else: 
            return dp[-1]
                    
