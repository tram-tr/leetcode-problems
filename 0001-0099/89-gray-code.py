# https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        def isPowerOfTwo(x):
            return x and (not(x & (x - 1)))

        def isDifferBy1bit(a,b):
            return isPowerOfTwo(a^b)

        res = []
        
        def dfs(curr, path, path_set):
            # print(path)
            if len(path) == 2 ** n:
                if isDifferBy1bit(path[0], path[-1]):
                    res.append(path[:])
                    return True

            for i in range(n):
                nxt = curr ^ (1 << i)
                if nxt not in path_set:
                    path.append(nxt)
                    path_set.add(nxt)
                    if dfs(nxt, path, path_set):
                        return True
                    path.pop()
                    path_set.remove(nxt)

            return False

        dfs(0, [0], set([0]))
        return res[0]
