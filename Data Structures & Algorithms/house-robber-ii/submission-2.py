class Solution:
    def rob1(self, nums):
        if not nums: return 0 # nums = [5] : nums[1:] = [], hence this case will arise.
        n = len(nums)
        if n == 1 : return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
