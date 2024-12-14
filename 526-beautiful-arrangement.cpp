class Solution {
public:
    int dfs(int n, vector<int>& visited) {
        if (n == 1)
            return 1;
        int count = 0;
        for (int i = 1; i < visited.size(); i++) {
            if (visited[i] == 0 && (n % i == 0 || i % n == 0)) {
                visited[i] = i;
                count += dfs(n - 1, visited);
                visited[i] = 0;
            }
        }
        return count;
    }

    int countArrangement(int n) {
        vector<int> visited(n + 1);
        return dfs(n, visited);
    }
};
