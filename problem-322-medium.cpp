class Solution {
public:
    int getChangeRec(vector<int>& coins, int curr, int amount) {
        // Time: O(2^N)
        // Space: O(N)
        if (curr == coins.size() || amount <= 0) {
            if (amount == 0)
                return 0;
            else return INT_MAX-1;
        }

        int count = -1;
        if (coins[curr] > amount)
            count = getChangeRec(coins, curr + 1, amount);
        else {
            count = min(1 + getChangeRec(coins, curr, amount - coins[curr]), getChangeRec(coins, curr + 1, amount));
        }

        return count;
    }

    int dp[12+1][10000+1];

    int getChangeDP(vector<int>& coins, int curr, int amount) {
        // Time: O(N*M)
        // Space: O(N*M)
        if (curr == coins.size() || amount <= 0) {
            if (amount == 0)
                return 0;
            else return INT_MAX-1;
        }
        // reduce recursive calls
        if (dp[curr][amount] > 0)
            return dp[curr][amount];
        
        if (coins[curr] > amount)
            dp[curr][amount] = getChangeDP(coins, curr + 1, amount);
        else {
            dp[curr][amount] = min(1 + getChangeDP(coins, curr, amount - coins[curr]), getChangeDP(coins, curr + 1, amount));
        }

        return dp[curr][amount];
    }

    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0)
            return 0;
        memset(dp, -1, sizeof(dp));
        int count = getChangeDP(coins, 0, amount);
        if (count == INT_MAX-1)
            return -1;
        else return count;
    }
};
