class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            toAdd = target - nums[i]
            if toAdd in res:
                return [res[toAdd], i]
            res[nums[i]] = i
        return []