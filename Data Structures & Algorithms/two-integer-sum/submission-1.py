class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            find_pair = target - nums[i]
            if find_pair in res.keys():
                return [res[find_pair], i]
            res[nums[i]] = i
        return -1