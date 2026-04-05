class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        for i in range(n):
            j = i+1
            while j<n and temperatures[j] <= temperatures[i]:
                j+=1
            res[i] = j-i if j < n else 0
        return res  