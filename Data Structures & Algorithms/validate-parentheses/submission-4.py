class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpenmap = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for c in s:
            if c in closeToOpenmap:
                if not stack or (stack[-1] != closeToOpenmap[c]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return True if not stack else False