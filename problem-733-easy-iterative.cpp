class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        // Time: O(N)
        // Space: O(N)
        if (image[sr][sc] == color)
            return image;
        
        // Iterative DFS
        stack<tuple<int, int>> frontier;
        vector<vector<int>> visited(image.size(), vector<int>(image[0].size(),0));

        int s_color = image[sr][sc];
        frontier.push(make_tuple(sr, sc));
      
        while (!frontier.empty()) {
            auto curr = frontier.top();
            frontier.pop();

            int row = get<0>(curr);
            int col = get<1>(curr);

            if (row < 0 || col < 0 || row >= image.size() || col >= image[0].size() || visited[row][col] == 1)
                continue;

            visited[row][col] = 1;

            if (image[row][col] == s_color) {
                image[row][col] = color;

                frontier.push(make_tuple(row + 1, col));
                frontier.push(make_tuple(row - 1, col));
                frontier.push(make_tuple(row, col + 1));
                frontier.push(make_tuple(row, col - 1));
            }
        }

        return image;
    }
};
