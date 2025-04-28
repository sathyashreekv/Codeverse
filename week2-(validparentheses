class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
        return len(stack) == 0
