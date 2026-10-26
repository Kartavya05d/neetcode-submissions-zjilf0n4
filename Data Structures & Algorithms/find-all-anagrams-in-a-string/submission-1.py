
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        pCount = [0] * 26
        sCount = [0] * 26

        for i in range(len(p)):
            pCount[ord(p[i]) - ord('a')] += 1
            sCount[ord(s[i]) - ord('a')] += 1

        res = [0] if pCount == sCount else []
        l = 0

        for r in range(len(p), len(s)):
            # Add the new character entering the window
            sCount[ord(s[r]) - ord('a')] += 1

            # Remove the character leaving the window
            sCount[ord(s[l]) - ord('a')] -= 1
            l += 1

            if pCount == sCount:
                res.append(l)

        return res
