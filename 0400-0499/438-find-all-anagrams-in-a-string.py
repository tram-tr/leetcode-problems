# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        counter = Counter(p)
        res = []
        left = 0
        for right in range(len(s)):
            counter[s[right]] -= 1
            while counter[s[right]] < 0:
                counter[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                res.append(left)

        return res

