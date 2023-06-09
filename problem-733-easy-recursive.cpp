class Solution {
public:
    # Recursive DFS
    # Time: O(N)
    # Space: O(N)
    void DFS_rec(vector<vector<int>>& image, int sr, int sc, int color, int s_color) {
        if (sr < 0 || sc < 0 || sr >= image.size() || sc >= image[0].size() || image[sr][sc] != s_color)
            return;
        image[sr][sc] = color;
        DFS_rec(image, sr + 1, sc, color, s_color);
        DFS_rec(image, sr - 1, sc, color, s_color);
        DFS_rec(image, sr, sc + 1, color, s_color);
        DFS_rec(image, sr, sc - 1, color, s_color);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        if (image[sr][sc] == color)
            return image;
        DFS_rec(image, sr, sc, color, image[sr][sc]);
        return image;
    }
};
