class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = set()
        maxx, left = 0, 0
        for right in range(len(s)):
            while s[right] in win:
                win.remove(s[left])
                left+=1
            win.add(s[right])
            maxx = max(maxx, len(win))
        return maxx