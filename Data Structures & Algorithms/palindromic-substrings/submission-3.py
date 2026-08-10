class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0 
        def expand(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
            return res
        for i in range(len(s)):
            #odd palindrome with s[i] as middle
            cnt += expand(i, i)
            #even
            cnt += expand(i, i+1)

        return cnt
