class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = 0 # xorr ^ A = A
        for i in range(n):
            xorr ^= i ^ nums[i]
        #Range is till n, but here we missed xorring with n.
        xorr ^= n
        return xorr
