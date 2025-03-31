# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        if not digits:
            return res
        def dfs(index, path):
            if index == len(digits):
                res.append(''.join(path))
                return 

            for c in digit_to_letters[digits[index]]:
                path.append(c)
                dfs(index + 1, path)
                path.pop()

            return

        dfs(0, [])

        return res
