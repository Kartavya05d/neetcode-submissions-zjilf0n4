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
            else:
                if stack:
                    last = stack.pop()
                    if openToCloseMap[last] != c:
                        return False
                else:
                    return False
        return True if not stack else False