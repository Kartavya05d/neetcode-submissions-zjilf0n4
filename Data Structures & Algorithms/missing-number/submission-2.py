class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n #because n won't be included in the loop.
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr
