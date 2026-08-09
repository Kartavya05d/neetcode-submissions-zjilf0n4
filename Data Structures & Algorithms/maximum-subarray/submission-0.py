class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, summ = float('-inf'), 0
        for num in nums:
            if summ < 0:
                summ = 0
            summ += num
            maxSum = max(maxSum, summ)
        return maxSum
