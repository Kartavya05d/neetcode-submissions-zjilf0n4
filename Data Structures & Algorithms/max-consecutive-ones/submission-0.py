class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        maxCons = 0
        for num in nums:
            if num:
                maxx += 1
                maxCons = max(maxx, maxCons)
            else:
                maxx = 0
        return maxCons