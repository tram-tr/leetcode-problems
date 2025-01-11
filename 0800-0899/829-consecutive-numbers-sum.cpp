class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int ans = 1, count;
        while (n % 2 == 0) n /= 2;
        for (int i = 3; i * i <= n; ans *= count + 1, i += 2)
            for (count = 0; n % i == 0; n /= i, count++);
        return n == 1 ? ans : ans * 2;
    }
};
