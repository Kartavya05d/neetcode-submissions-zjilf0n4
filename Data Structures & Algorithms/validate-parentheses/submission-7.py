class Solution:
    def isValid(self, s: str) -> bool:
        openToCloseMap = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = []
        for c in s:
            if c in openToCloseMap:
                stack.append(c)
            elif stack:
                if openToCloseMap[stack[-1]] != c:
                    return False
                stack.pop()
            else:
                return False
        return True if not stack else False