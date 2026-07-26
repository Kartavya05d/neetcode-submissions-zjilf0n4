class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            mini = min(mini, prices[i])
            maxx = max(prices[i]-mini, maxx)
        return maxx
