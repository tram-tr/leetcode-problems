# https://leetcode.com/problems/decode-the-message/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hmap = {} # ordered set
        hmap[' '] = ' '
        i = 0
        for c in key:
            if c not in hmap:
                hmap[c] = chr(ord('a') + i)
                i += 1
        
        decode = ''
        for c in message:
            decode += hmap[c]

        return decode
