# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = [word[::-1] for word in words]
        return ' '.join(words)
