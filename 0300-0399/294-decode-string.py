# https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        '''
        s = "3[a2[c]]"
        stack = (3,'')
        res = ''
        curr_num = 3

        stack = (3,''), (2, 'a')
        res = a
        curr_num = 2

        stack = (3,''), (2,'a')
        res = c
        curr_num = 0

        stack = (3,'')
        prev_num = 2
        prev_str = 'a'
        res = a + 2 * c = acc
        curr_num = 0

        stack = 
        prev_num = 3
        prev_str = ''
        res =  + 3 * acc = accaccacc
        curr_num = 0

        '''
        res = ''
        stack = []
        curr_num = 0

        for i in range(len(s)):
            if s[i] == '[':
                stack.append((curr_num, res))
                res = ''
                curr_num = 0
            elif s[i] == ']':
                prev_num, prev_str = stack.pop()
                res = prev_str + prev_num * res
            elif s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            else:
                res += s[i]

        return res
