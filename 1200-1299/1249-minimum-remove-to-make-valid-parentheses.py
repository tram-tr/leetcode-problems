# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0
        for c in s:
            if c == ')' and count == 0:
                continue
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            stack.append(c)

        res = []
        count = 0
        for c in stack[::-1]: # reverse stack
            if c == '(' and count == 0:
                continue
            if c == ')':
                count += 1
            elif c == '(':
                count -= 1
            res.append(c)

        return ''.join(res[::-1])
        
