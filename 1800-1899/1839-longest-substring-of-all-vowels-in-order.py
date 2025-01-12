# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        left = 0
        count = 1
        
        for right in range(1, len(word)):
            if ord(word[right]) < ord(word[right - 1]):
                count = 1
                left = right
            elif ord(word[right]) > ord(word[right - 1]):
                count += 1
            
            if count == 5 and word[right] == 'u':
                res = max(res, right - left + 1)

        return res
