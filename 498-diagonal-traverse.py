# https://leetcode.com/problems/diagonal-traverse/description/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        traverse = defaultdict(list)
        for i in range(m):
            for j in range(n):
                traverse[i + j].append(mat[i][j])

        res = []
        for key, values in traverse.items():
            if key % 2 == 0:
                values.reverse()
            res.extend(values)

        return res
        
