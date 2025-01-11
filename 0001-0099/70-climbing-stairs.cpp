class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2)
            return n;

        // Time: O(N)
        // Space: O(N)
        /*vector<int> dp(n+1);
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++)
            dp[i] = dp[i-1] + dp[i-2];
        return dp[n];*/

        // Time: O(N)
        // Space: O(1)
        int pprev = 0;
        int prev = 1;
        for (int i = 1; i <= n; i++) {
            int curr = prev + pprev;
            pprev = prev;
            prev = curr;
        }
        return prev;
    }
};
