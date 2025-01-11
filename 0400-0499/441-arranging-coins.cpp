class Solution {
public:
    int arrangeCoins(int n) {
        if (n < 2)
            return n;
        int rows = 0;
        while (n >= 0) {
            rows++;
            n -= rows;
        }
        return rows-1;
    }
};
