class Solution:
    def isValid(self, s: str) -> bool:
        map = { ')': '(', ']': '[', '}': '{' }
        stack = []
        for c in s:
            if c not in map:
                stack.append(c)
            else:
                if not stack or map.get(c) != stack[-1]:
                    return False
                stack.pop()
        return len(stack) == 0
