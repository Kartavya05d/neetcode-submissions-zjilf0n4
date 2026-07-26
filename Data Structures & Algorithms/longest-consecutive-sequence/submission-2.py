class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = 0
        maxCnt = 0
        for num in nums:
            if num-1 not in nums: #this is start of sequence.
                cnt = 1
                while num+1 in nums:
                    num+=1
                    cnt+=1
                maxCnt = max(maxCnt, cnt)
        return maxCnt
