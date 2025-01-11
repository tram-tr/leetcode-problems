# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        left = 0
        res = 0
        max_occur = 0
        for right in range(len(s)):
            window[s[right]] += 1
            max_occur = max(max_occur, window[s[right]])
            while (right - left + 1) - max_occur > k:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
