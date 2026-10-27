class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        tC, win = {}, {}

        for c in t:
            tC[c] = tC.get(c, 0) + 1
        
        have, need = 0, len(tC)
        res, resLen = [-1,-1], float('infinity')
        l =0
        for r in range(len(s)):
            c = s[r]
            win[c] = win.get(c, 0)+1
            if c in tC and win[c] == tC[c]:
                have += 1
            while have == need:
                stringLen = r-l+1
                if stringLen < resLen:
                    res, resLen = [l, r], stringLen
                win[s[l]] -= 1
                if s[l] in tC and win[s[l]] < tC[s[l]]:
                    have-=1
                l+=1
            
        l, r = res
        return s[l:r+1] if resLen != float('infinity') else ""