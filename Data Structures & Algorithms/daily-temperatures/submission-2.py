class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, currTemp in enumerate(temperatures):
            while stack and stack[-1][0] < currTemp: #current temp is warmer
                temp, idx = stack.pop()
                res[idx] = i - idx
            stack.append((currTemp, i))
        return res
