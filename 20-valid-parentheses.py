class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket) # push to the stack
            else:
                if len(stack) == 0: # corner case 1: there is no open bracket in the current stack
                    return False
                top = stack[-1] # pop the top of the stack (LIFO order)
                stack.pop()
                if (bracket == ')' and top != '(') or (bracket == ']' and top != '[') or (bracket == '}' and top != '{'):
                    return False

        return len(stack) == 0 # corner case 2: there are open brackets remaining in the stack
