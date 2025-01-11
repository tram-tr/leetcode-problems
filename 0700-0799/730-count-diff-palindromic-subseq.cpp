class Solution {
public:
    int MOD = pow(10,9)+7;
    int Mem[1001][1001][4];
    int dp(int left, int right, int alpha, string &s) {
        if (left > right)
            return 0;
        if ((left == right) && s[left] == (alpha + 'a'))
            return 1;
        if (Mem[left][right][alpha] != -1)
            return Mem[left][right][alpha];

        int count = 0;
        if (s[left] == s[right] && s[left] == (alpha + 'a')) {
            count = 2;
            for (int i = 0; i < 4; i++)
                count = (count + dp(left + 1, right - 1, i, s)) % MOD;
        } else {
            count = (count + dp(left, right - 1, alpha, s)) % MOD;
            count = (count + dp(left + 1, right, alpha, s)) % MOD;
            count = (count - dp(left + 1, right - 1, alpha, s)) % MOD;
            if (count < 0)
                count += MOD;
        }
        Mem[left][right][alpha] = count;

        return count;
    }
    int countPalindromicSubsequences(string s) {
        memset(Mem, -1, sizeof(Mem));
        int ans = 0;
        for (int i = 0; i < 4; i++) 
            ans = (ans + dp(0, s.size()-1, i, s)) % MOD;
        return ans;
    }
};
