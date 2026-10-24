class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]
            #if each element is converted to right most.
            #current [we haven't actually transformed] total + k
            if nums[r]*(r-l+1) > total + k: #invalid condition
                total -= nums[l]
                l+=1
        return len(nums)-l
