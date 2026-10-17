class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        res, currSum = 0, 0

        for num in nums:
            currSum += num

            if currSum == k: res+=1
            if currSum-k in prefixSum:
                res += prefixSum[currSum-k]
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        return res
