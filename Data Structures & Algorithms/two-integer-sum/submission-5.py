class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh = {}

        for i, num in enumerate(nums):
            toAdd = target-num
            if toAdd in hashh:
                return [hashh[toAdd], i]
            hashh[num] = i
        return [-1,-1]