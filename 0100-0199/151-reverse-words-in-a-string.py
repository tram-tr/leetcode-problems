# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        res = []

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])

        return ' '.join(res)
