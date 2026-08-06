class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def expand(t1, t2):
            nonlocal res, resLen

            while t1 >= 0 and t2 < len(s) and s[t1] == s[t2]:
                if (t2 - t1 + 1) > resLen:
                    res = s[t1:t2 + 1]
                    resLen = t2 - t1 + 1
                t1 -= 1
                t2 += 1

        for i in range(len(s)):
            expand(i, i)      # odd length
            expand(i, i + 1)  # even length

        return res
