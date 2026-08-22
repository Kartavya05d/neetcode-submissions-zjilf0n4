class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n%2 #if odd, one will be remainder
            n = n >> 1
        return cnt
    
