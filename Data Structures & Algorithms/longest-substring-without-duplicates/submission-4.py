class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = set()
        maxx, left = 0, 0

        for r in range(len(s)):
            while s[r] in win:
                win.remove(s[left])
                left+=1
            win.add(s[r])
            maxx = max(maxx, len(win))
        return maxx
