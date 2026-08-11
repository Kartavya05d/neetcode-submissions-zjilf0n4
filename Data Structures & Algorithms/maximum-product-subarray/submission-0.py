class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMin * num
            curMin = min(num*curMax, num*curMin, num)
            curMax = max(num*curMax, tmp, num)
            res = max(res, curMax)
        return res
