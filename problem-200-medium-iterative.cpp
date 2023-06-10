class Solution {
public:
    void dfs (vector<vector<char>>& grid, int sr, int sc) {
        stack<tuple<int,int>> frontier;
        frontier.push(make_tuple(sr,sc));
        while (!frontier.empty()) {
            auto curr = frontier.top();
            frontier.pop();
            auto row = get<0>(curr);
            auto col = get<1>(curr);

            if (row < 0 || col < 0 || row >= grid.size() || col >= grid[0].size())
                continue;
            if (grid[row][col] != '1')
                continue;

            grid[row][col] = '*';
            frontier.push(make_tuple(row + 1, col));
            frontier.push(make_tuple(row - 1, col));
            frontier.push(make_tuple(row, col + 1));
            frontier.push(make_tuple(row, col - 1));
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j ++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
};
