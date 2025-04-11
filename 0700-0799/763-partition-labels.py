# https://leetcode.com/problems/partition-labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = defaultdict(int)
        for i in range(len(s)):
            last_occur[s[i]] = i

        res = []
        l = r = 0
        for i in range(len(s)):
            r = max(r, last_occur[s[i]])
            if i == r:
                res.append(r - l + 1)
                l = i + 1
            
        return res
