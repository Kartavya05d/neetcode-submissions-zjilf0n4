class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            j = 0
            p = 1
            while j < len(nums):
                if j != i:
                    p = p*nums[j]
                j += 1
            res.append(p)
        return res