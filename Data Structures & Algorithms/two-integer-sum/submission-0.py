class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        for i in range(len(nums)):
            findFor = target-nums[i]
            if findFor in l.keys():
                return [l[findFor],i]
            l[nums[i]] = i
