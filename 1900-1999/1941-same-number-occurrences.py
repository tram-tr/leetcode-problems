# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # hmap = {}
        # for c in s:
        #     hmap[c] = hmap.get(c, 0) + 1

        hmap = Counter(s)
        
        return len(set(hmap.values())) == 1
