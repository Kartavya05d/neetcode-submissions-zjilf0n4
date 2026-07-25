class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            toAdd = target - nums[i]
            if toAdd in hashmap:
                return [hashmap[toAdd], i]
            hashmap[nums[i]] = i
