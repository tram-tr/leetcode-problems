# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # count = 0
        # for w in words:
        #     w = set(w)
        #     if w.issubset(allowed):
        #         count += 1
        # return count

        count = 0 # count for non-consistent
        for w in words:
            for c in w:
                if c not in allowed:
                    count += 1
                    break
        return len(words) - count
